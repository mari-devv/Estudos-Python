
#criando as listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
#veio com a lista c que é a junção da lista a + b
lista_c = lista_a + lista_b
# .extend vai realizar a extensão da lista a + a lista b
lista_a.extend(lista_b)
#printa a lista com a extensão
print(lista_a)