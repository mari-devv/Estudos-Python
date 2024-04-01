"""
Exercício
Exiba os indices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Clara')
for nome in enumerate(lista):
    print(nome)