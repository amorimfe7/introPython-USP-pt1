import math

x1=int(input("Digite o primeiro número:"))
y1=int(input("Digite o segundo número:"))
x2=int(input("Digite o terceiro número:"))
y2=int(input("Digite o quarto número:"))

delta_x= (x2 - x1)
delta_y= (y2 - y1)

distancia = math.sqrt((delta_x**2) + (delta_y**2))
print(distancia)

if (distancia >= 10):
    print("longe")
else:
    print("perto")