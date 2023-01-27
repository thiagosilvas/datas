import calendar
import datetime
import time



semanas = []
dias_do_mes = []




cal= calendar.Calendar()
hoje = datetime.date.today()
datadehoje = str(hoje.year)+"-"+str(hoje.month)+"-"+str(hoje.day)




for dias in cal.itermonthdates(hoje.year,hoje.month):
    data = str(dias)
    if dias.month == hoje.month:
        dias_do_mes.append(str(dias))


calculo = len(dias_do_mes)/7


condicao = 0

while condicao <= calculo:
    remova = dias_do_mes[:7]
    semanas.append(remova)
    for remover in remova:
        dias_do_mes.remove(remover)
 
    condicao += 1    
  
    
for i,semana in enumerate(semanas):
    print("Semana:" , i+1,semana)