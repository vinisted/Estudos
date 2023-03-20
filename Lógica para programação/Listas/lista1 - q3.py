#Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original da 
#dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25). 

v_divida = float(input("Digite o valor original da dívida: "))
d_atraso = float(input("Digite a quantidade de dias em atraso: "))
v_multa = float(input("Digite o valor da multa por dia: "))

calc_multa = d_atraso * v_multa + v_divida

print("O valor da dívida mais a multa é de R$ {}".format(calc_multa))