"""
slipt e join com list e str
split - divide uma string
join - une uma string
strip() - corta os espaços do meio e do inicio da string
rstrip() - lstrip() |  r = right | l = left
"""

frase = 'Olha só, que coisa interessante'
        #Escolhi oque vai separar minha frase split(',')
lista_frase = frase.split(',')

for i, frase in  enumerate(lista_frase):
    lista_frase[i] = lista_frase[i].strip()

print(lista_frase)