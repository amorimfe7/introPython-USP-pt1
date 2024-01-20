#recebe um número inteiro e imprime seu dígito das dezenas

numero_int=int(input("Digite um número inteiro:"))
div= (numero_int//10)
digito_dezena= (div%10)

print("O dígito das dezenas é",digito_dezena)
