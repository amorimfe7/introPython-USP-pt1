nmr_inteiro=int(input("Digite um número inteiro:"))

if((nmr_inteiro % 5) == 0) and ((nmr_inteiro % 3) == 0):
    print("FizzBuzz")
else:
    print(nmr_inteiro)