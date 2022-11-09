import matplotlib
import pandas

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import nltk
from nltk import tokenize
import seaborn as sns
from wordcloud import WordCloud

nltk.download('movie_reviews')
nltk.download('punkt')

token_espaco = tokenize.WhitespaceTokenizer()


def mostrar_contagem_citacoes(dataframe, termos_candidatos: dict) -> None:
    df = pandas.melt(dataframe, value_vars=list(termos_candidatos.keys()), var_name='candidato', value_name='citacoes')
    plt.subplots(figsize=(20, 10))
    grafico = sns.countplot(data=df.loc[df['citacoes'] == 1], x='candidato', color="#ffa500")
    grafico.set_xlabel('Candidato')
    grafico.set_ylabel('Número de citações')
    grafico.set_title("Total de menções por candidato")
    sns.set(font_scale=1)
    for p in grafico.patches:
        grafico.annotate(p.get_height(), (p.get_x() + 0.25, p.get_height() + 0.01))
    plt.show()


def mostrar_citacoes_por_semana(dataframe, termos_candidatos: dict) -> None:
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
    df3.plot(figsize=(20, 10),
             lw=3,
             kind='line',
             style='s:',
             title="Menções por semana")
    plt.xlabel('Semana')
    plt.ylabel('Número de citações')
    plt.legend(title='Candidato', bbox_to_anchor=(1, 1))
    plt.show()


def mostrar_citacoes_por_dia(dataframe, termos_candidatos: dict) -> None:
    df = pandas.DataFrame(columns=['dia', 'candidato', 'quantidade'])
    dias_analise = dataframe['dia'].astype(str).unique()
    for dia in dias_analise:
        for candidato in termos_candidatos.keys():
            df2 = dataframe.query(f'dia == "{dia}" & {candidato} == 1')
            quantidade = len(df2.index)
            df = pandas.concat([df, pandas.DataFrame.from_records([{
                'dia': dia,
                'candidato': candidato,
                'quantidade': quantidade
            }])])
    df3 = df.pivot(index='dia', columns='candidato', values='quantidade')
    df3.plot(figsize=(20, 10),
             lw=3,
             kind='line',
             style='s:',
             title="Menções por dia")
    plt.xlabel('Dia')
    plt.ylabel('Número de citações')
    plt.legend(title='Candidato', bbox_to_anchor=(1, 1))
    plt.show()


def mostrar_rival_natural(dataframe, termos_candidatos: dict) -> None:
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
    df = df[:10]
    df.set_index('candidatos', inplace=True)
    df.plot(figsize=(20, 10),
            kind='barh',
            title="Maiores menções em conjunto (""Rivais Naturais"")").legend(loc='upper center')
    plt.xlabel('Número de citações')
    plt.ylabel('Rivais naturais')
    plt.xticks(rotation=0, horizontalalignment="center")
    plt.show()


def mostrar_grafico_palavras(dataframe, quantidade: int):
    todas_palavras = ' '.join([texto for texto in dataframe['texto']])
    token_frase = token_espaco.tokenize(todas_palavras)
    frequencia = nltk.FreqDist(token_frase)
    df_frequencia = pandas.DataFrame({"palavra": list(frequencia.keys()), "frequencia": list(frequencia.values())})
    df_frequencia.nlargest(columns="frequencia", n=quantidade)
    df_frequencia = df_frequencia.nlargest(columns="frequencia", n=10)
    plt.figure(figsize=(15, 10))
    grafico = sns.barplot(data=df_frequencia, x="palavra", y="frequencia")
    grafico.set(ylabel="Contagem")
    grafico.set_title("Total de citações por candidato")
    plt.show()


def mostrar_nuvem_palavras(dataframe):
    todas_palavras = ' '.join([texto for texto in dataframe.texto_tratado.astype(str)])
    nuvem_palavras = WordCloud(width=2000,
                               height=1000,
                               colormap="Dark2",
                               background_color="#fefff2",
                               collocations=False).generate(todas_palavras)

    plt.figure(figsize=(20, 10))
    plt.imshow(nuvem_palavras, interpolation='bilinear')
    plt.axis("off")
    plt.title("Palavras mais usadas durante as eleições no Twitter")
    plt.show()


def mostrar_tweets_unicos_ou_conjunto(dataframe):
    quantidade_tweets_unicos = len(dataframe.query('mais_de_um_candidato == 0'))
    quantidade_tweets_conjunto = len(dataframe.query('mais_de_um_candidato == 1'))

    qtde = [quantidade_tweets_unicos, quantidade_tweets_conjunto]
    legenda = 'Único', 'Conjunto'
    cores = ["#e7c137", "#a6d1ff"]
    explosao = [0.1, 0]
    fig, chart = plt.subplots(figsize=(10, 8))
    chart.pie(qtde,
              labels=legenda,
              autopct='%1.1f%%',
              colors=cores,
              explode=explosao,
              startangle=90,
              shadow=True)
    chart.set_title("Menções dos candidatos")
    plt.legend(title="")
    plt.show()


def mostrar_mais_tweets_positivos(dataframe, termos_candidatos: dict):
    dataframe_filtrado = dataframe.query('mais_de_um_candidato == 0 & classificacao > 0')
    df = pandas.melt(dataframe_filtrado, value_vars=list(termos_candidatos.keys()), var_name='candidato',
                     value_name='citacoes')
    plt.subplots(figsize=(20, 10))
    grafico = sns.countplot(data=df.loc[df['citacoes'] == 1], x='candidato', color="#23C552")
    grafico.set_xlabel('Candidato')
    grafico.set_ylabel('Número de citações positivas')
    grafico.set_title("Total de citações positivas")
    sns.set(font_scale=1)
    for p in grafico.patches:
        grafico.annotate(p.get_height(), (p.get_x() + 0.25, p.get_height() + 0.01))
    plt.show()


def mostrar_mais_tweets_negativos(dataframe, termos_candidatos: dict):
    dataframe_filtrado = dataframe.query('mais_de_um_candidato == 0 & classificacao < 0')
    df = pandas.melt(dataframe_filtrado, value_vars=list(termos_candidatos.keys()), var_name='candidato',
                     value_name='citacoes')
    plt.subplots(figsize=(20, 10))
    grafico = sns.countplot(data=df.loc[df['citacoes'] == 1], x='candidato', color="#F84F31")
    grafico.set_xlabel('Candidato')
    grafico.set_ylabel('Número de citações negativas')
    grafico.set_title("Total de citações negativas")
    sns.set(font_scale=1)
    for p in grafico.patches:
        grafico.annotate(p.get_height(), (p.get_x() + 0.25, p.get_height() + 0.01))
    plt.show()


def mostrar_tweets_positivos_por_semana(dataframe, termos_candidatos: dict) -> None:
    dataframe_filtrado = dataframe.query('mais_de_um_candidato == 0 & sentimento > 0')
    df = pandas.DataFrame(columns=['semana', 'candidato', 'quantidade'])
    semanas_analise = dataframe_filtrado['semana_analise'].unique()
    for semana in semanas_analise:
        for candidato in termos_candidatos.keys():
            df2 = dataframe_filtrado.query(f'semana_analise == {semana} & {candidato} == 1')
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


def mostrar_volumetria_classificacao_candidato(dataframe, candidato: str):
    quantidade_neutro, quantidade_positivo, quantidade_negativo = 0, 0, 0
    df_candidato = dataframe.query(f'{candidato} == 1 & mais_de_um_candidato == 0')
    for classificacao in df_candidato['classificacao'].astype(float):
        if classificacao > 0:
            quantidade_positivo += 1
            continue
        if classificacao < 0:
            quantidade_negativo += 1
            continue
        quantidade_neutro += 1

    legenda = 'Positivo', 'Negativo', 'Neutro'
    cores = ["#23C552", "#F84F31", "#808080"]
    quantidade_geral = [quantidade_positivo, quantidade_negativo, quantidade_neutro]

    fig, chart = plt.subplots(figsize=(10, 8))

    chart.pie(quantidade_geral,
              labels=legenda,
              autopct='%1.1f%%',
              colors=cores,
              shadow=True)
    chart.set_title("Sentimentos")
    plt.legend(title="Sentimento")
    plt.show()


def mostrar_volumetria_classificacao_geral(dataframe, termo_candidatos: dict):
    quantidade_neutro, quantidade_positivo, quantidade_negativo = 0, 0, 0
    query_candidatos = ' | '.join(list(map(lambda candidato: f'{candidato} == 1', list(termo_candidatos.keys()))))
    df_candidato = dataframe.query(f'({query_candidatos}) & mais_de_um_candidato == 0')
    for classificacao in df_candidato['classificacao'].astype(float):
        if classificacao > 0:
            quantidade_positivo += 1
            continue
        if classificacao < 0:
            quantidade_negativo += 1
            continue
        quantidade_neutro += 1

    legenda = 'Positivo', 'Negativo', 'Neutro'
    cores = ["#23C552", "#F84F31", "#808080"]
    quantidade_geral = [quantidade_positivo, quantidade_negativo, quantidade_neutro]

    fig, chart = plt.subplots(figsize=(10, 8))

    chart.pie(quantidade_geral,
              labels=legenda,
              autopct='%1.1f%%',
              colors=cores,
              shadow=True)
    chart.set_title("Sentimentos")
    plt.legend(title="Sentimento")
    plt.show()
