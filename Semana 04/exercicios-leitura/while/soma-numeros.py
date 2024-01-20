print("Digite uma sequência de números | Digite [0] para finalizar ")

numero = 1
soma = 0

while numero != 0:
    numero = int(input("Digite um valor a ser somado: "))
    soma = soma + numero

print(soma)