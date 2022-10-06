from typing import List

import pandas
import matplotlib
matplotlib.use('TkAgg')
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

print(dataframe.head())

dataframe['mes'] = dataframe['data_tweet'].dt.month

dataframe['semana_ano'] = dataframe['data_tweet'].map(lambda data: int(data.strftime("%V")))

dataframe['semana_analise'] = dataframe['semana_ano'] - 22

for chave, valor in termos_candidatos.items():
    termos_regex = '|'.join(valor)
    dataframe[chave] = dataframe['texto'].str.contains(pat=fr'(?:{termos_regex.lower()})', case=False).map({True: 1,
                                                                                                            False: 0})

dataframe.to_excel('bases/base-menor-tratada.xlsx')


# def mostrar_contagem_citacoes() -> None:
#     todas_citacoes = {}
#     for candidato in termos_candidatos.keys():
#         contagem = 0
#         if candidato not in todas_citacoes:
#             todas_citacoes[candidato] = 0
#         for tags in dataframe.tags:
#             if candidato in tags:
#                 contagem += 1
#         todas_citacoes[candidato] = contagem
#     todas_citacoes = {k: v for k, v in todas_citacoes.items() if v > 0}
#
#     plt.pie(todas_citacoes.values(), labels=todas_citacoes.keys())
#     plt.show()

