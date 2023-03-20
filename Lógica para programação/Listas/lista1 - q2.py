#Faça um programa que calcule a média de consumo (em km/l) de combustível de um veículo. O usuário deve informar o KM 
#inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso. 

km_inicial = float(input("Digite o Km inicial: "))
km_final = float(input('Digite o km final: '))
consumo = float(input('Digite o consumo em litros gastos no percurso: '))

calc_consumo = (km_final-km_inicial)/consumo

print("Seu veículo consome em média {:0.2f} litros por Km.".format(calc_consumo))