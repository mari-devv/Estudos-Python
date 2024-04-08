"""
Imprecisão de ponto flutuante e maneiras de contornar

formatando o número
round

"""


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)  #0.799999999999
print(f'{numero_3:.2f}') # 0.80
print(round(numero_3, 3)) # 0.8