#se delta <0 == esta equação nao possui raizes reais
#se delta == 0 == a raiz é > valor raiz
#se delta >0 == as raízes da equacao são: 1 e 2 raiz
#formula de bhaskara

def bhaskara(a,b,c):
    delta = (b**2 - 4*a*c)

    if delta == 0:
        r1 = -b+m.sqrt(delta)/(2*a)
        print("A raíz é:",r1)
    elif delta < 0:
        import math as m
        txt = print("Esta equação não possui raízes reais")
    else:
        import math as m
        r1 = -b+m.sqrt(delta)/(2*a)
        r2 = -b-m.sqrt(delta)/(2*a)
        txt = print("As raizes são:", r1,r2)
        return r1,r2,txt

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

delta = (b**2 - 4*a*c)

if delta == 0:
    print("A raíz é:",bhaskara(a,b,c))
elif delta < 0:
    print("Esta equação não possui raízes reais")
else:
    txt = print("As raizes são:", bhaskara(a,b,c))