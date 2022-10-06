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

dataframe = pandas.read_excel('bases/base-menor.xlsx')

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
    print(df)
    grafico = sns.countplot(data=df.loc[df['citacoes'] == 1], x='candidato')
    grafico.set_xlabel('Candidato')
    grafico.set_ylabel('Número de citações')
    plt.show()


mostrar_contagem_citacoes()

