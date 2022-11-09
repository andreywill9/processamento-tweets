import graficos
import constantes
import pandas

dataframe_segundo_turno = pandas.read_excel('bases/turno_2_tratado.xlsx')
graficos.mostrar_citacoes_por_dia(dataframe_segundo_turno, constantes.termos_candidatos_segundo_turno)
