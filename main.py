import graficos
import constantes
import pandas

dataframe_primeiro_turno = pandas.read_excel('bases/turno_1_tratado.xlsx')
dataframe_segundo_turno = pandas.read_excel('bases/turno_2_tratado.xlsx')
dataframe_eleicao_completa = pandas.read_excel('bases/periodo_eleitoral_completo_tratado.xlsx')
dataframe_pesquisa_completa = pandas.read_excel('bases/pesquisa_completa_tratado.xlsx')


# graficos.mostrar_contagem_citacoes(dataframe_primeiro_turno, constantes.termos_todos_candidatos,
#                                    'Citações por candidato 1º turno')

# graficos.mostrar_contagem_citacoes(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
#                                    'Citações por candidato 2º turno')

# graficos.mostrar_contagem_citacoes(dataframe_eleicao_completa, constantes.termos_todos_candidatos,
#                                    'Citações por candidato (periodo eleitoral completo)')


# graficos.mostrar_citacoes_por_semana(dataframe_primeiro_turno, constantes.termos_todos_candidatos,
#                                      'Citações por semana (1º turno)')

# graficos.mostrar_citacoes_por_dia(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
#                                   'Citações por dia (2° turno)')

graficos.mostrar_citacoes_por_semana(dataframe_pesquisa_completa, constantes.termos_candidatos_segundo_turno,
                                     'Evolução citações Lula e Bolsonaro (por semana)', candidato_unico=True)


graficos.mostrar_grafico_palavras(dataframe_eleicao_completa, 10, 'Top 10 palavras mais usadas durante a eleição')


graficos.mostrar_nuvem_palavras(dataframe_eleicao_completa, 'Palavras mais usadas durante a eleição')

graficos.mostrar_nuvem_palavras(dataframe_primeiro_turno, 'Palavras mais usadas durante o 1º turno')

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas durante o 2º turno')

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas em Tweets Positivos (1º turno)',
                                data_inicial=constantes.inicio_primeiro_turno, data_final=constantes.fim_primeiro_turno,
                                positivo=True)

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas em Tweets Negativos (1º turno)',
                                data_inicial=constantes.inicio_primeiro_turno, data_final=constantes.fim_primeiro_turno,
                                negativo=True)

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas em Tweets Positivos (2º turno)',
                                data_inicial=constantes.inicio_segundo_turno, data_final=constantes.fim_segundo_turno,
                                positivo=True)

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas em Tweets Negativos (2º turno)',
                                data_inicial=constantes.inicio_segundo_turno, data_final=constantes.fim_segundo_turno,
                                negativo=True)


graficos.mostrar_mais_tweets_positivos(dataframe_eleicao_completa, constantes.termos_todos_candidatos,
                                       'Candidatos com mais Tweets positivos')

graficos.mostrar_mais_tweets_negativos(dataframe_eleicao_completa, constantes.termos_todos_candidatos,
                                       'Candidatos com mais Tweets negativos')


graficos.mostrar_tweets_unicos_ou_conjunto(dataframe_pesquisa_completa)


graficos.mostrar_volumetria_classificacao_geral(dataframe_pesquisa_completa, constantes.termos_todos_candidatos,
                                                'Sentimento geral das eleições')

graficos.mostrar_volumetria_classificacao_geral(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
                                                'Sentimento geral do 2º turno')


graficos.mostrar_rival_natural(dataframe_primeiro_turno, constantes.termos_todos_candidatos)


graficos.mostrar_evolucao_classificacao(dataframe_pesquisa_completa, 'lula',
                                        'Evolução de Tweets positivos do candidato Lula',
                                        positivo=True)

graficos.mostrar_evolucao_classificacao(dataframe_pesquisa_completa, 'lula',
                                        'Evolução de Tweets negativos do candidato Lula',
                                        negativo=True)


graficos.mostrar_evolucao_classificacao(dataframe_pesquisa_completa, 'bolsonaro',
                                        'Evolução de Tweets positivos do candidato Bolsonaro',
                                        positivo=True)

graficos.mostrar_evolucao_classificacao(dataframe_pesquisa_completa, 'bolsonaro',
                                        'Evolução de Tweets negativos do candidato Bolsonaro',
                                        negativo=True)

