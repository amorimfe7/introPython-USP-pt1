#receba qtnd de segundos, "quebre" esse valor em dias, horas, minutos e segundos
#A saída deve estar no formato: a dias, b horas, c minutos e d segundos
# 1 dia = 86400s
# 1 hora = 3600s
# 1 minuto = 60s

segundos_str=input("Por favor, entre com o número de segundos que deseja converter:")
total_segs = int(segundos_str)
a = (total_segs//86400) #pois queremos ele inteiro DIAS primeiro
resto_segs_dia = (total_segs%86400)

b= (resto_segs_dia//3600) #pois queremos a qntd em HORAS
resto_segs_horas = (resto_segs_dia%3600)

c= (resto_segs_horas//60)
resto_segs_minuto = (resto_segs_horas%60)

d= (resto_segs_minuto % 60)

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
