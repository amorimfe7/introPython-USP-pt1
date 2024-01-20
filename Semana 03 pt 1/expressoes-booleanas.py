##Teste para praticar - EXPRESSÕES BOOLEANAS

#Ex 01 - Resultado sem vai ver TRUE
x = 9999999999
result01=(x>0) or (x<=0)
print("Expressão 01", result01)

#Ex 04
x=5
y=3
z=7
result02= x > y and x < z
print("Expressão 02", result02)

#Ex 05
idade=15
maioridade=18
podeDirigir= idade >= maioridade
print("Expressão 05", podeDirigir)

#Ex 07
x=10
y=15
z=25
result07=(x == z - y and z!= y - x or not y != z - x)
print("Expressão 07", result07)

#Ex 08
x=10
y=20
z=30
result08=(not y<10 or not z==10)
print("Expressão 08",result08)

#Ex 08_2
x=10
y=20
z=30
result08_2=(x<=30 and y>=5)
print("Expressão 08_2",result08_2)

x=10
y=20
z=30
result08_3=(x >= 10 or y != z - x)
print("Expressão 08_3",result08_3)

#Ex 10
a=1
b=2
print("Expressão 10",a!=2 or b ==1)