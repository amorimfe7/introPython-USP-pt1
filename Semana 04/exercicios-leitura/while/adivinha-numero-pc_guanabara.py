import random

print("Tente adivinhar o número que o PC está pensando..")

nmr_digitado = int(input("Digite um número de 0 a 10: "))

numero = random.randint(0,10)
palpite = 0

while nmr_digitado != numero:
    nmr_digitado = int(input("Tente novamente, digite seu número: "))
    palpite = palpite + 1
    

if nmr_digitado == numero:
    print("Parabéns, você acertou!")
    print("Você realizou",palpite,"tentativas")