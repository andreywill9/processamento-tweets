import graficos
import constantes
import pandas

dataframe_primeiro_turno = pandas.read_excel('bases/turno_1_tratado.xlsx')
dataframe_segundo_turno = pandas.read_excel('bases/turno_2_tratado.xlsx')
dataframe_eleicao_completa = pandas.read_excel('bases/periodo_eleitoral_completo_tratado.xlsx')
dataframe_pesquisa_completa = pandas.read_excel('bases/pesquisa_completa_tratado.xlsx')

graficos.mostrar_contagem_citacoes(dataframe_primeiro_turno, constantes.termos_todos_candidatos,
                                   'Citações por candidato 1º turno')

graficos.mostrar_contagem_citacoes(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
                                   'Citações por candidato 2º turno')

graficos.mostrar_citacoes_por_semana(dataframe_primeiro_turno, constantes.termos_todos_candidatos,
                                     'Evolução dos candidatos no 1º turno (por semana)', candidato_unico=True)

graficos.mostrar_citacoes_por_dia(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
                                  'Citações por dia (2° turno)', candidato_unico=True)

graficos.mostrar_grafico_palavras(dataframe_eleicao_completa, 10,
                                  'Top 10 palavras mais usadas durante a eleição (pré tratamento)')

graficos.mostrar_nuvem_palavras(dataframe_eleicao_completa, 'Palavras mais usadas durante a eleição')

graficos.mostrar_nuvem_palavras(dataframe_primeiro_turno, 'Palavras mais usadas durante o 1º turno')

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas durante o 2º turno')

graficos.mostrar_nuvem_palavras(dataframe_primeiro_turno, 'Palavras mais usadas em Tweets Positivos (1º turno)',
                                data_inicial=constantes.inicio_primeiro_turno, data_final=constantes.fim_primeiro_turno,
                                positivo=True)

graficos.mostrar_nuvem_palavras(dataframe_primeiro_turno, 'Palavras mais usadas em Tweets Negativos (1º turno)',
                                data_inicial=constantes.inicio_primeiro_turno, data_final=constantes.fim_primeiro_turno,
                                negativo=True)

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas em Tweets Positivos (2º turno)',
                                data_inicial=constantes.inicio_segundo_turno, data_final=constantes.fim_segundo_turno,
                                positivo=True)

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno, 'Palavras mais usadas em Tweets Negativos (2º turno)',
                                data_inicial=constantes.inicio_segundo_turno, data_final=constantes.fim_segundo_turno,
                                negativo=True)

graficos.mostrar_nuvem_palavras(dataframe_primeiro_turno,
                                'Palavras mais usadas na semana do Debate da Rede Globo (1º turno)',
                                data_inicial=constantes.inicio_debate_globo_primeiro_turno,
                                data_final=constantes.fim_debate_globo_primeiro_turno)

graficos.mostrar_nuvem_palavras(dataframe_segundo_turno,
                                'Palavras mais usadas na semana do Debate da Rede Globo (2º turno)',
                                data_inicial=constantes.inicio_debate_globo_segundo_turno,
                                data_final=constantes.fim_debate_globo_segundo_turno)

graficos.mostrar_mais_tweets_positivos(dataframe_eleicao_completa, constantes.termos_todos_candidatos,
                                       'Candidatos com mais Tweets positivos')

graficos.mostrar_mais_tweets_negativos(dataframe_eleicao_completa, constantes.termos_todos_candidatos,
                                       'Candidatos com mais Tweets negativos')

graficos.mostrar_tweets_unicos_ou_conjunto(dataframe_pesquisa_completa)

graficos.mostrar_volumetria_classificacao_geral(dataframe_pesquisa_completa, constantes.termos_todos_candidatos,
                                                'Sentimento geral das eleições')

graficos.mostrar_volumetria_classificacao_geral(dataframe_primeiro_turno, constantes.termos_todos_candidatos,
                                                'Sentimento geral do 1º turno')

graficos.mostrar_volumetria_classificacao_geral(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
                                                'Sentimento geral do 2º turno')

graficos.mostrar_rival_natural(dataframe_primeiro_turno, constantes.termos_todos_candidatos)

graficos.mostrar_volumetria_classificacao_candidato(dataframe_eleicao_completa, 'lula',
                                                    'Sentimento geral sobre candidato Lula')

graficos.mostrar_volumetria_classificacao_candidato(dataframe_eleicao_completa, 'bolsonaro',
                                                    'Sentimento geral sobre candidato Bolsonaro')

graficos.mostrar_volumetria_classificacao_candidato(dataframe_eleicao_completa, 'ciro',
                                                    'Sentimento geral sobre candidato Ciro')

graficos.mostrar_volumetria_classificacao_candidato(dataframe_eleicao_completa, 'simone_tebet',
                                                    'Sentimento geral sobre candidata Simone Tebet')

graficos.mostrar_citacoes_por_dia_candidato(dataframe_segundo_turno, 'lula',
                                            'Evolução de Tweets positivos do candidato Lula (2º turno)', positivo=True,
                                            data_inicial=constantes.inicio_segundo_turno,
                                            data_final=constantes.fim_segundo_turno)

graficos.mostrar_citacoes_por_dia_candidato(dataframe_segundo_turno, 'lula',
                                            'Evolução de Tweets negativos do candidato Lula (2º turno)', negativo=True,
                                            data_inicial=constantes.inicio_segundo_turno,
                                            data_final=constantes.fim_segundo_turno)

graficos.mostrar_citacoes_por_dia_candidato(dataframe_segundo_turno, 'bolsonaro',
                                            'Evolução de Tweets positivos do candidato Bolsonaro (2º turno)',
                                            positivo=True,
                                            data_inicial=constantes.inicio_segundo_turno,
                                            data_final=constantes.fim_segundo_turno)

graficos.mostrar_citacoes_por_dia_candidato(dataframe_segundo_turno, 'bolsonaro',
                                            'Evolução de Tweets negativos do candidato Bolsonaro (2º turno)',
                                            negativo=True,
                                            data_inicial=constantes.inicio_segundo_turno,
                                            data_final=constantes.fim_segundo_turno)

graficos.mostrar_citacoes_por_dia(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
                                  'Evolução Tweets positivos (2° turno)', candidato_unico=True, positivo=True)

graficos.mostrar_citacoes_por_dia(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno,
                                  'Evolução Tweets negativos (2° turno)', candidato_unico=True, negativo=True)
