sexo = input("Digite seu sexo: | [M/F/NB]").upper()

while sexo != 'M' and sexo != 'F' and sexo != 'NB':
    sexo = input("Digite um sexo válido: ").upper()

if sexo == 'M':
    print("O sexo escolhido foi MASCULINO")
if sexo == 'F':
    print("O sexo escolhido foi FEMININO")
if sexo == 'NB':
    print("Você se identificou como NÃO BINÁRIO")


