numero = int(input("Digite um número natural positivo: "))

contagem=1

while contagem <= (numero+numero):
    if contagem % 2 !=0:
        print(contagem)
        contagem = contagem + 1
    else:
        contagem = contagem + 1