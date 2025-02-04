import datetime

data_e_hora_atual = datetime.datetime.now()
print(data_e_hora_atual)

ano = data_e_hora_atual.year
mes = data_e_hora_atual.month
dia = data_e_hora_atual.day
hora = data_e_hora_atual.hour
minuto = data_e_hora_atual.minute
segundo = data_e_hora_atual.second

print(ano, mes, dia, hora, minuto, segundo)
