x = int(input("Digite um número natural positivo: "))

soma = 0

while x != 0:
    ultimo_dig = (x % 10) #4 #3 #2 #1
    x = (x - ultimo_dig)//10 #123 #12 #1
    soma = soma + ultimo_dig # 0 = 0 + 4

    #soma1 = soma + 4 == 4
    #soma2 = 4 + 3 == 7
    #soma3 = 7 + 2 == 9
    #soma4 = 9 + 1 == 10

print(soma)
