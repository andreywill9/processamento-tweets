from constantes import arroba_candidato
from constantes import stopwords
from constantes import abreviacoes
from constantes import palavras_irrelevantes
from constantes import palavras_classificadas
from constantes import termos_todos_candidatos
from constantes import token_espaco
import pandas
import nltk
import re
import unidecode
import spacy
import itertools
from datetime import datetime

nltk.download('movie_reviews')
nltk.download('punkt')

nlp = spacy.load("pt_core_news_lg")


def tratar_base(dataframe: pandas.DataFrame):
    dataframe['texto'] = dataframe['texto'].astype(str)
    dataframe['texto'] = dataframe.texto.str \
        .lower() \
        .replace(r'[^\w\s@]', '', regex=True) \
        .replace(r'[\s]+', ' ', regex=True)
    frases_processadas = list()
    for opiniao in dataframe["texto"]:
        if opiniao is None or len(opiniao) == 0:
            continue
        nova_frase = list()
        mencoes_tweet = re.findall("@[A-Za-z0-9_]+", opiniao)
        outras_mencoes = list(filter((lambda x: x not in arroba_candidato), mencoes_tweet))
        palavras_texto2 = opiniao.split(' ')
        for palavra in palavras_texto2:
            if palavra in outras_mencoes or palavra in stopwords or set(
                    abreviacoes[palavra].split(' ') if palavra in abreviacoes.keys() else [palavra]).issubset(stopwords):
                continue
            if palavra in arroba_candidato:
                nova_frase.append(arroba_candidato[palavra])
                continue
            palavra = unidecode.unidecode(palavra)
            if palavra in palavras_irrelevantes:
                continue
            nova_frase.extend(abreviacoes[palavra].split(' ') if palavra in abreviacoes.keys() else [palavra])
        doc = nlp(' '.join(nova_frase))
        nova_frase = list()
        for palavra in doc:
            nova_frase.append(palavra.lemma_.lower())
        frases_processadas.append(' '.join(nova_frase))
    dataframe['texto_tratado'] = frases_processadas
    dataframe['data_tweet'] = pandas.to_datetime(dataframe['data_tweet']) \
        .dt.tz_localize(None)
    dataframe['mes'] = dataframe['data_tweet'].dt.month
    dataframe['dia'] = dataframe['data_tweet'].map(lambda data: f'{str(data.day).zfill(2)}/{str(data.month).zfill(2)}')
    dataframe['semana_ano'] = dataframe['data_tweet'].map(lambda data: int(data.strftime("%V")))
    dataframe['semana_analise'] = dataframe['semana_ano'] - 22
    for chave, valor in termos_todos_candidatos.items():
        termos_regex = '|'.join(valor)
        dataframe[chave] = dataframe['texto_tratado'].str.contains(pat=fr'(?:{termos_regex.lower()})', case=False).map(
            {True: 1,
             False: 0})
    dataframe['mais_de_um_candidato'] = dataframe['lula'] + dataframe['bolsonaro'] + dataframe['ciro'] \
                                        + dataframe['simone_tebet'] + dataframe['eymael'] \
                                        + dataframe['sofia_manzano'] + dataframe['soraya_thronicke'] \
                                        + dataframe['felipe_d_avila'] + dataframe['vera_lucia'] \
                                        + dataframe['leo_pericles']
    dataframe['mais_de_um_candidato'] = dataframe['mais_de_um_candidato'] > 1
    dataframe.sort_values(by='data_tweet', inplace=True)


def aplicar_analise_sentimentos(dataframe: pandas.DataFrame):
    polaridade_tweets = []
    nomes_candidatos = itertools.chain.from_iterable(termos_todos_candidatos.values())
    for tweet in dataframe['texto_tratado'].astype(str):
        pontuacao_tweet = 0
        palavras = tweet.split()
        quantidade_mencoes = len(list(filter(lambda x: x in nomes_candidatos, palavras)))
        for palavra in palavras:
            if palavra in palavras_classificadas:
                pontuacao_tweet += palavras_classificadas[palavra] * (1 / (len(palavras) - quantidade_mencoes))
        polaridade_tweets.append(obter_pontuacao(pontuacao_tweet))
    dataframe['classificacao'] = polaridade_tweets


def obter_pontuacao(pontuacao_calculada):
    if pontuacao_calculada == 0:
        return 0
    if pontuacao_calculada < -1:
        return -2
    if pontuacao_calculada < 0:
        return -1
    if pontuacao_calculada < 1:
        return 1
    return 2


def salvar_palavras_mais_usadas(dataframe: pandas.DataFrame, caminho_saida: str):
    todas_palavras = ' '.join([texto for texto in dataframe['texto_tratado'].astype(str)])
    token_frase = token_espaco.tokenize(todas_palavras)
    frequencia = nltk.FreqDist(token_frase)
    df_frequencia = pandas.DataFrame({"palavra": list(frequencia.keys()), "frequencia": list(frequencia.values())})
    df_frequencia.to_excel(caminho_saida)


inicio_execucao = datetime.now()
print(f'Incicio da execução: {inicio_execucao}')
dataframes = {
    'turno_1': pandas.read_excel('bases/turno_1.xlsx'),
    'turno_2': pandas.read_excel('bases/turno_2.xlsx'),
    'periodo_eleitoral_completo': pandas.read_excel('bases/periodo_eleitoral_completo.xlsx'),
    'pre_eleitoral': pandas.read_excel('bases/pre_eleitoral.xlsx'),
    'pesquisa_completa': pandas.read_excel('bases/pesquisa_completa.xlsx')
}
for nome_dataframe in dataframes:
    print(f'Iniciando {nome_dataframe}...')
    tratar_base(dataframes[nome_dataframe])
    aplicar_analise_sentimentos(dataframes[nome_dataframe])
    dataframes[nome_dataframe].to_excel(f'bases/{nome_dataframe}_tratado.xlsx')
    print(f'{nome_dataframe} tratado!!')
fim_execucao = datetime.now()
print(f'Fim da execução: {fim_execucao}')
