#regras p/ determinar se um ano é bissexto ou não são
#o ano deve ser divisível por 4 e não divisível por 100, exceto para os divisíveis por 400

ano = int(input('Digite o ano: '))
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('O ano:','"',ano,'"', 'é bissexto')
    
else:
        print('O ano que foi digitado não é bissexto.')
    
    

