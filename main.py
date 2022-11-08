import graficos
import pandas

dataframe_segundo_turno = pandas.read_excel('bases/turno_2_tratado.xlsx')
graficos.mostrar_nuvem_palavras(dataframe_segundo_turno)
