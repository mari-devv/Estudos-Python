def verifica_numero(numero):
    if numero % 2 != 0:
        print("Estranho")
    else:
        if numero >= 2 and numero <= 5:
            print("Not Weird")
        elif numero >= 6 and numero <= 20:
            print("Estranho")
        elif numero > 20:
            print("Not Weird")

# Exemplo de uso
numero = int(input("Digite um número inteiro: "))
verifica_numero(numero)
