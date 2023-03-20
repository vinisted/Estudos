#Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro
#ele deseja abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.

valor = float(input('Digite o valor do combustível: '))
quanto = float(input('Digite quanto em dinheiro você deseja abastecer: '))

c_litros = quanto / valor

print("A quantidade de combustível em litros é de: {:0.2f} litros.".format(c_litros))