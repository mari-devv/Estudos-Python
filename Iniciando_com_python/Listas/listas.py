"""
Listas em python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend,

Create Read Update Delete CRUD
Criar, ler, alterar, apagar = lista[i]   (CRUD)

string = 'ABCDE' # 5 caracteres len()
lista = [123, True, 'Clara', 1.2, []]
print(lista)

#print(bool([]))  - falsy
#print(lista, type(lista))
"""
#   +01234
#   -54321
# Tudo em Python é um objeto
"""del lista[2]
print(lista)"""

lista = [10, 20, 30, 40]
# .appende adiciona um item a lista
lista.append(50)
# .pop retira um item da lista / ele retira o ultimo valor
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)





