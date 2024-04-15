"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import random 



for _ in range(100):
    cpf9 = ''   

    for i in range(9):
        cpf9 += str(random.randint(0,9))
    print(f'Número antes {cpf9}')
    numeros_mult = 0
    contador = 10

    for numeros in cpf9:
        numeros = int(numeros)
        numeros_mult += numeros * contador
        contador = contador - 1
    digito1 = (numeros_mult * 10)  %11
    digito1 = 0 if digito1 > 9 else digito1
    print(f'O primeiro digito é: {digito1}')

    digito2 = str(cpf9) + str(digito1)
    numeros_mult2 = 0
    contador2 = 11

    for numeros2 in digito2:
        numeros2 = int(numeros2)
        numeros_mult2 += numeros2 * contador2
        contador2 = contador2 - 1
    digito2 = (numeros_mult2 * 10)  %11
    digito2 = 0 if digito2 > 9 else digito2
    print(f'O segundo digito é: {digito2}')
    print(f'Número formatado {cpf9}{digito1}{digito2}')

