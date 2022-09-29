from typing import List

import pandas
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def obter_tags(texto_tweet: str) -> List[str]:
    tags_tweet = []
    for candidato, termos in termos_candidatos.items():
        if any(map((lambda termo: termo in texto_tweet), termos)):
            tags_tweet.append(candidato)
    return tags_tweet

# LIMPEZA

termos_candidatos = {
    'Lula': ['lula', 'luiz inacio lula da silva'],
    'Bolsonaro': ['bolsonaro', 'jair messias bolsonaro'],
    'Ciro': ['ciro', 'ciro gomes'],
    'Simone Tebet': ['tebet', 'simone tebet'],
    'Eymael': ['eymael', 'eymael o democrata cristao'],
    'Sofia Manzano': ['sofia manzano', 'manzano pcb'],
    'Soraya Thronicke': ['soraya thronicke', 'soraya união brasil'],
    'Felipe D’Avila': ['felipe davila', 'felipe davila novo'],
    'Vera Lúcia': ['vera lucia','vera lucia pstu'],
    'Leo Péricles': ['leo pericles', 'leonardo pericles']
}


dataframe = pandas.read_excel('bases/base-menor.xlsx')

dataframe['texto'] = dataframe.texto.str\
    .lower()\
    .replace(r'[^\w\s@]', '', regex=True)\
    .replace(r'[\n | \t]', ' ', regex=True)\
    .replace(r'[\s]+', ' ', regex=True)

dataframe['data_tweet'] = pandas.to_datetime(dataframe['data_tweet'])\
    .dt.tz_localize(None)

dataframe['mes'] = dataframe['data_tweet'].map(lambda data: data.month)

dataframe['semana_ano'] = dataframe['data_tweet'].map(lambda data: int(data.strftime("%V")))

dataframe['semana_analise'] = dataframe['semana_ano'] - 22

dataframe['tags'] = dataframe['texto'].map(obter_tags)


def mostrar_contagem_citacoes() -> None:
    todas_citacoes = {}
    for candidato in termos_candidatos.keys():
        contagem = 0
        if candidato not in todas_citacoes:
            todas_citacoes[candidato] = 0
        for tags in dataframe.tags:
            if candidato in tags:
                contagem += 1
        todas_citacoes[candidato] = contagem
    todas_citacoes = {k: v for k, v in todas_citacoes.items() if v > 0}

    plt.pie(todas_citacoes.values(), labels=todas_citacoes.keys())
    plt.show()


mostrar_contagem_citacoes()

