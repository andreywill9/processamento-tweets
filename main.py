from typing import List

import pandas

# LIMPEZA

termos_candidatos = {
    'Lula': ['lula', 'luiz inacio lula da silva'],
    'Bolsonaro': ['bolsonaro', 'jair messias bolsonaro']
}

def obter_tags(texto_tweet: str) -> List[str]:
    tags_tweet = []
    for candidato, termos in termos_candidatos.items():
        if any(map((lambda termo: termo in texto_tweet), termos)):
            tags_tweet.append(candidato)
    return tags_tweet


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

dataframe.to_excel('bases/base-menor-tratada.xlsx')
