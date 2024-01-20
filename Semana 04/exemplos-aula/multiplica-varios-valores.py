
tamanho_sequencia = int(input("Digite o tamanho da sequência de números:"))
multiplicacao=1
i=0

while i < tamanho_sequencia:
    valor = int(input("Digite um valor a ser multiplicado:"))
    multiplicacao = multiplicacao * valor
    i = i + 1

print("O produto dos valores digitados é:", multiplicacao)
