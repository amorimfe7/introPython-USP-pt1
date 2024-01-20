#receber entrada de dados do tipo STRING, recebendo nome do cliente,
#dia de vencimento, o mês de vencimento e o valor da fatura
#e imprima, a saudação e o nome na linha1 e
#na linha2
#A sua fatura com vencimento em X de XXXXX no valor de R$ XXX,XX está fechada.

nome_cliente=(input("Digite o nome do cliente:"))
dia_vencimento=(input("Digite o dia do vencimento:"))
mes_vencimento=(input("Digite o mês do vencimento:"))
valor_fatura=(input("Digite o valor da fatura:"))

print("Olá,",nome_cliente)
print("A sua fatura com vencimento em",dia_vencimento,"de",mes_vencimento,"no valor de R$",valor_fatura,"está fechada.")
