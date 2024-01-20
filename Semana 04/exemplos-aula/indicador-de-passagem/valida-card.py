userCard = int(input("Digite o número do seu Cartão: "))

cardVerificados = 1
cardEncontrado = False

while cardVerificados != 0 and not cardEncontrado: #cardEcontrado aqui será verdadeiro, pois, inicia-se em False
    cardVerificados = int(input("Digite o número do Cartão que deseja verificar: "))
    if cardVerificados == userCard:
        cardEncontrado = True

if cardEncontrado == True:
    print("Cartão encontrado!")
else:
    print("Cartão não foi encontrado! :(")