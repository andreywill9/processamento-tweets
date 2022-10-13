from typing import List

import pandas
import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import matplotlib.pyplot as plt

# LIMPEZA

termos_candidatos = {
    'lula': ['lula', 'luiz inacio lula da silva'],
    'bolsonaro': ['bolsonaro', 'jair messias bolsonaro'],
    'ciro': ['ciro', 'ciro gomes'],
    'simone_tebet': ['tebet', 'simone tebet'],
    'eymael': ['eymael', 'eymael o democrata cristao'],
    'sofia_manzano': ['sofia manzano', 'manzano pcb'],
    'soraya_thronicke': ['soraya thronicke', 'soraya união brasil'],
    'felipe_d_avila': ['felipe davila', 'felipe davila novo'],
    'vera_lucia': ['vera lucia','vera lucia pstu'],
    'leo_pericles': ['leo pericles', 'leonardo pericles']
}

dataframe = pandas.read_excel('bases/base-completa.xlsx')

dataframe['texto'] = dataframe.texto.str\
    .lower()\
    .replace(r'[^\w\s@]', '', regex=True)\
    .replace(r'[\n | \t]', ' ', regex=True)\
    .replace(r'[\s]+', ' ', regex=True)

dataframe['data_tweet'] = pandas.to_datetime(dataframe['data_tweet'])\
    .dt.tz_localize(None)

dataframe['mes'] = dataframe['data_tweet'].dt.month

dataframe['semana_ano'] = dataframe['data_tweet'].map(lambda data: int(data.strftime("%V")))

dataframe['semana_analise'] = dataframe['semana_ano'] - 22

for chave, valor in termos_candidatos.items():
    termos_regex = '|'.join(valor)
    dataframe[chave] = dataframe['texto'].str.contains(pat=fr'(?:{termos_regex.lower()})', case=False).map({True: 1,
                                                                                                            False: 0})


def mostrar_contagem_citacoes() -> None:
    df = pandas.melt(dataframe, value_vars=list(termos_candidatos.keys()), var_name='candidato', value_name='citacoes')
    grafico = sns.countplot(data=df.loc[df['citacoes'] == 1], x='candidato')
    grafico.set_xlabel('Candidato')
    grafico.set_ylabel('Número de citações')
    plt.show()
    plt.close()


def mostrar_citacoes_por_mes() -> None:
    df = pandas.DataFrame(columns=['semana', 'candidato', 'quantidade'])
    semanas_analise = dataframe['semana_analise'].unique()
    for semana in semanas_analise:
        for candidato in termos_candidatos.keys():
            df2 = dataframe.query(f'semana_analise == {semana} & {candidato} == 1')
            quantidade = len(df2.index)
            df = pandas.concat([df, pandas.DataFrame.from_records([{
                'semana': semana,
                'candidato': candidato,
                'quantidade': quantidade
            }])])
    df3 = df.pivot(index='semana', columns='candidato', values='quantidade')
    df3.plot()
    plt.xlabel('Semana')
    plt.ylabel('Número de citações')
    plt.legend(title='Candidato', bbox_to_anchor=(1, 1))
    plt.show()


def mostrar_rival_natural() -> None:
    df = pandas.DataFrame(columns=['candidatos', 'citacoes'])
    df.set_index('candidatos')
    for candidato in termos_candidatos.keys():
        for candidato2 in termos_candidatos.keys():
            combinacao = f'{candidato} e {candidato2}'
            combinacao_invertida = f'{candidato2} e {candidato}'
            if candidato == candidato2 or combinacao in df.candidatos.values or combinacao_invertida in df.candidatos.values:
                continue
            df2 = dataframe.query(f'{candidato} == 1 & {candidato2} == 1')
            contagem = len(df2.index)
            df = pandas.concat([df, pandas.DataFrame.from_records([{
                'candidatos': f'{candidato} e {candidato2}',
                'citacoes': contagem
            }])])
    df = df.sort_values(by='citacoes', ascending=False, ignore_index=True)
    df = df[:5]
    df.set_index('candidatos', inplace=True)
    df.plot(kind='barh')
    plt.xlabel('Número de citações')
    plt.ylabel('Rivais')
    plt.xticks(rotation=0, horizontalalignment="center")
    plt.show()


mostrar_contagem_citacoes()
mostrar_citacoes_por_mes()
mostrar_rival_natural()
