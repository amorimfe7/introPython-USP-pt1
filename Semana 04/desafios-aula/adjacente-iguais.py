numero = int(input("Digite um número inteiro: "))

verifica = False

#1234
while numero > 0 and not verifica: # enquanto verifica é TRUE
    ultimo_dig = (numero % 10) #ultimo digito #4
    numero = (numero - ultimo_dig)//10 #outros digitos #123
    ultimo_dig2 = (numero % 10) #segundo digito #3
    if ultimo_dig == ultimo_dig2:
        verifica = True

if verifica:
    print("Sim! Há números adjacentes iguais no número inserido")
else:
    print("Não! Há números adjacentes iguais no número inserido")
    
