import math

#se delta <0 == esta equação nao possui raizes reais
#se delta == 0 == a raiz é > valor raiz
#se delta >0 == as raízes da equacao são: 1 e 2 raiz
#formula de bhaskara
a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta= (b**2 - 4*a*c)

if  delta == 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    print("A raíz é:",x1)
elif delta < 0:
    print("Esta equação não possui raízes reais") 
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("As raízes da equação são:",x1,"e",x2)



  