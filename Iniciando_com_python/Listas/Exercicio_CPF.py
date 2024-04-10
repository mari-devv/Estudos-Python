"""CPF: 746.824.890-70
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
# CPF fornecido
cpf = "746.824.890-70"

# Remover pontos, traços e converter para uma lista de inteiros
cpf_numeros = [int(digito) for digito in cpf if digito.isdigit()]

# Multiplicar cada dígito do CPF pelo índice + 1
produtos = [a * (b + 1) for a, b in zip(cpf_numeros[:9], range(9))]

# Calcular a soma dos produtos
soma = sum(produtos)

# Calcular o primeiro dígito verificador
primeiro_digito = soma * 10 % 11

# Verificar se o primeiro dígito é maior que 9
if primeiro_digito < 10:
    primeiro_digito_cpf = primeiro_digito
else:
    primeiro_digito_cpf = 0

print("Primeiro dígito do CPF:", primeiro_digito_cpf)
