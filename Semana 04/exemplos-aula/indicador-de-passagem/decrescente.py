
valor1 = int(input("Digite o 1º valor da sequência: "))
prox_valor =1
decrescente = True

while valor1 !=0 and decrescente:
    prox_valor = int(input("Digite o próximo valor da sequência: "))
    if prox_valor > valor1:
        decrescente = False
    valor1 = prox_valor

if decrescente == True:
    print("A sequência é DECRESCENTE!")
else:
    print("A sequência não é DECRESCENTE")