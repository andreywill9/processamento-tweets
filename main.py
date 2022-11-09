import graficos
import constantes
import pandas
from datetime import datetime

dataframe_segundo_turno = pandas.read_excel('bases/turno_2_tratado.xlsx')
data_inicial = datetime(year=2022, month=10, day=2)
data_final = datetime(year=2022, month=10, day=3)
graficos.mostrar_nuvem_palavras_periodo(dataframe_segundo_turno, data_inicial, data_final, 'Palavras mais usadas na semana do Debate')
