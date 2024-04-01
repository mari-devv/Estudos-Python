# lista vazia
numero = []
valor = 5
# loop vai ser executado 6 vezes
# cada vez que esse loop for executado o valor atual de "valor" vai ser adicionado á lista numero que esta vazia
# a cada loop vai ser adicionado o numero 2
# apos o loop a lista numeros terá os valore [5, 7, 9, 11, 13, 15] 
for x in range (6):
 numero.append (valor)
 #x = x + valor
 valor += 2
print (numero [1] + numero [5])
