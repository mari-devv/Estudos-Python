#!/usr/bin/env python
num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

operacao = input('Escolha: + - * /: ')

if operacao == '+':
    print(f'O resultado é: {num1 + num2}')
elif operacao == '-':
    print(f'O resultado é: {num1 - num2}')
elif operacao == '*':
    print(f'O resultado é: {num1 * num2}')
elif operacao == '/':
    print(f'O resultado é: {num1 / num2}')
else:
    print('OPERAÇÃO INVALIDA')