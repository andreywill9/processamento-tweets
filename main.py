import pandas
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import nltk
from nltk import tokenize
import seaborn as sns
import re
import unidecode
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import spacy
from string import punctuation

nltk.download('movie_reviews')
nltk.download('punkt')

nlp = spacy.load("pt_core_news_lg")

token_espaco = tokenize.WhitespaceTokenizer()

# LIMPEZA

termos_candidatos = {
    'lula': ['lula', 'luiz inacio lula da silva', '@lulaoficial'],
    'bolsonaro': ['bolsonaro', 'jair messias bolsonaro', '@jairbolsonaro'],
    'ciro': ['ciro', 'ciro gomes', '@cirogomes'],
    'simone_tebet': ['tebet', 'simone tebet', '@simonetebetbr'],
    'eymael': ['eymael', 'eymael o democrata cristao', '@eymaelpr2022'],
    'sofia_manzano': ['sofia manzano', 'manzano pcb', '@sofiamanzanopcb'],
    'soraya_thronicke': ['soraya thronicke', 'soraya união brasil', '@sorayathronicke'],
    'felipe_d_avila': ['felipe davila', 'felipe davila novo', '@fdavilaoficial'],
    'vera_lucia': ['vera lucia', 'vera lucia pstu', '@verapstu'],
    'leo_pericles': ['leo pericles', 'leonardo pericles', '@leopericlesup']
}

arroba_candidato = {'@lulaoficial': 'lula',
                    '@jairbolsonaro': 'bolsonaro',
                    '@cirogomes': 'ciro',
                    '@simonetebetbr': 'simone_tebet',
                    '@eymaelpr2022': 'eymael',
                    '@sofiamanzanopcb': 'sofia_manzano',
                    '@sorayathronicke': 'soraya_thronicke',
                    '@fdavilaoficial': 'felipe_d_avila',
                    '@verapstu': 'vera_lucia',
                    '@leopericlesup': 'leo_pericles'}

abreviacoes = {
    'vc': 'voce',
    'vcs': 'voces',
    'pq': 'porque',
    'pra': 'para',
    'pro': 'para o',
    'q': 'que',
    'mn': 'mano',
    'blz': 'beleza',
    'pdc': 'pode crer',
    'gnt': 'gente',
    'mds': 'meu deus',
    'vlw': 'valeu',
    'hj': 'hoje',
    'tar': 'estar',
    'lix': 'lixo',
    'nd': 'nada',
    'pfv': 'por favor',
    'hrs': 'horas',
    'aq': 'aqui',
    'pft': 'perfeito',
    'glr': 'galera',
    'clr': 'celular',
    'n': 'nao',
    's': 'sim',
    'ctz': 'certeza',
    'dps': 'depois',
    'dnv': 'denovo',
    'msm': 'mesmo',
    'sla': 'sei la',
    'ngm': 'ninguem',
    'p': 'para'
}

stopwords = nltk.corpus.stopwords.words("portuguese")
palavras_irrelevantes = [*punctuation] + stopwords
token_pontuacao = tokenize.WordPunctTokenizer()

dataframe = pandas.read_excel('bases/base-menor.xlsx')

dataframe['texto'] = dataframe.texto.str \
    .lower() \
    .replace(r'[^\w\s@]', '', regex=True) \
    .replace(r'[\s]+', ' ', regex=True)

frases_processadas = list()
for opiniao in dataframe["texto"]:
    nova_frase = list()
    palavras_texto = token_pontuacao.tokenize(opiniao)
    for palavra in palavras_texto:
        nova_frase.extend(abreviacoes[palavra].split(' ') if palavra in abreviacoes.keys() else [palavra])
    frases_processadas.append(' '.join(nova_frase))
dataframe['texto'] = frases_processadas

mencoes_candidatos = list()
candidatos = list()

tweets_tratados = list()
for opiniao in dataframe.texto:
    mencoes_tweet = re.findall("@[A-Za-z0-9_]+", opiniao)
    outras_mencoes = list(filter((lambda x: x not in arroba_candidato), mencoes_tweet))

    for mencao in outras_mencoes:
        opiniao = opiniao.replace(mencao, '')
    for arroba in arroba_candidato.keys():
        opiniao = opiniao.replace(arroba, arroba_candidato[arroba])

    nova_frase = list()
    palavras_texto = token_espaco.tokenize(opiniao)
    for palavra in palavras_texto:
        if palavra not in stopwords:
            nova_frase.append(palavra)
    tweets_tratados.append(' '.join(nova_frase))

dataframe["tratamento_1"] = tweets_tratados

sem_acentos = [unidecode.unidecode(texto) for texto in dataframe["tratamento_1"]]
dataframe["tratamento_2"] = sem_acentos

frases_processadas = list()
for opiniao in dataframe["tratamento_2"]:
    nova_frase = list()
    palavras_texto = token_pontuacao.tokenize(opiniao)
    for palavra in palavras_texto:
        if palavra not in palavras_irrelevantes:
            nova_frase.append(palavra)
    frases_processadas.append(' '.join(nova_frase))

dataframe["tratamento_2"] = frases_processadas

frases_processadas = list()
for opiniao in dataframe["tratamento_2"]:
    nova_frase = list()
    doc = nlp(opiniao)
    for palavra in doc:
        nova_frase.append(palavra.lemma_.lower())
    frases_processadas.append(' '.join(nova_frase))

dataframe["tratamento_3"] = frases_processadas

dataframe['data_tweet'] = pandas.to_datetime(dataframe['data_tweet']) \
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


def mostrar_grafico_palavras(quantidade):
    todas_palavras = ' '.join([texto for texto in dataframe['tratamento_3']])
    token_frase = token_espaco.tokenize(todas_palavras)
    frequencia = nltk.FreqDist(token_frase)
    df_frequencia = pandas.DataFrame({"palavra": list(frequencia.keys()), "frequencia": list(frequencia.values())})
    df_frequencia.nlargest(columns="frequencia", n=quantidade)
    df_frequencia = df_frequencia.nlargest(columns="frequencia", n=10)
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(data=df_frequencia, x="palavra", y="frequencia")
    ax.set(ylabel="Contagem")
    plt.show()


def mostrar_nuvem_palavras():
    todas_palavras = ' '.join([texto for texto in dataframe.tratamento_3])
    nuvem_palavras = WordCloud(width=1500,
                               height=800,
                               max_font_size=200,
                               collocations=False).generate(todas_palavras)

    plt.figure(figsize=(10, 7))
    plt.imshow(nuvem_palavras, interpolation='bilinear')
    plt.axis("off")
    plt.show()


mostrar_contagem_citacoes()
mostrar_citacoes_por_mes()
mostrar_rival_natural()
mostrar_grafico_palavras(10)
mostrar_nuvem_palavras()

