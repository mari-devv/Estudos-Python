"""
Introdução ao empacotamento e desempacotamento
"""
"""
# Lista
minha_lista = [1, 2, 3, 4, 5]
minha_lista[0] = 10  # A lista pode ser modificada
print(minha_lista)  # Saída: [10, 2, 3, 4, 5]

# Tupla
minha_tupla = (1, 2, 3, 4, 5)
# minha_tupla[0] = 10  # Isso causaria um erro, as tuplas são imutáveis
print(minha_tupla)  # Saída: (1, 2, 3, 4, 5)

Usar listas quando precisar de uma coleção de itens mutáveis e use tuplas quando precisar de uma coleção de itens imutáveis.

"""

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)