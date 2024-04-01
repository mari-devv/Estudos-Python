#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
# mês com 21 dias

salario_horas = float(input('Insira seu salario por hora: '))
horas_trabalhadas = float(input('Insira a quantidade de horas trabalhadas: '))

total_salario = salario_horas * horas_trabalhadas

total_mes = total_salario * 21

print(f'O total do salario é : {total_mes}')