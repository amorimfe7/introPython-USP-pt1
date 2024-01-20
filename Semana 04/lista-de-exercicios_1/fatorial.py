nmr_recebido=int(input("Digite um número natural: "))

fatorial=1

while (nmr_recebido > 0):
    fatorial = fatorial * nmr_recebido
    nmr_recebido = nmr_recebido - 1 

print(fatorial)

#f 1 = 1 * 5 ==5
#nmr 5 = 5 - 1 ==4

#f 5 = 5* 4 ==20
#nmr 4 = 4 - 1 ==3

#f 20 = 20* 3 == 60
#nmr 3 = 3 - 1 ==2

#f 60 = 60 * 2 == 120
#nmr 2 = 2 - 1 == 1

#f 120 = 120 * 1== 120
#nmr 1 = 1 - 1 == 0

