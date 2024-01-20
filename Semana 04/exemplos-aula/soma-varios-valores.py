print("Digite uma sequência de valores para soma | Digite [0] para finalizar a soma")

soma=0
valor=1

while valor !=0:
    valor = int(input("Digite um valor a ser somado:"))
    soma = soma + valor

print("A soma dos valores digitados é:", soma)
