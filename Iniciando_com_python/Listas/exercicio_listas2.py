"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
#criou uma lista vazia
lista = []
# O while vai fazer a verificação, se o usuário escolher algumas das opções abaixo o programa continua.
while True:
    #Printa a "interface"
    print('Selecione uma opção')
    #Abre o input para escolher a opção
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    #Caso a opção escolhida seja igual á 'i' ele continua a operação de INSERT
    if opcao == 'i':  
        os.system('cls')
        #Abre o input para inserir o valor
        valor = input('Valor: ')
        # .append vai realizar a adição na ultima colocação da lista.
        lista.append(valor)
    #Caso a opção escolhida seja igual á 'a' ele continua a operação de DELETE
    elif opcao == 'a':
        #Printa a parte da escolha para deletar o indice que o usuário escolher.
        indice_str = input(
            'Escolha o índice para apagar: '
        )
        # TRY - EXCEPT vai lidar com as exceções
        try:
            #Essa linha tenta converter a variável em um número inteiro e atribui o resultado à variável se a variavel não puder ser convertida em int, Vai gerar a exceção do tipo 'ValueError'
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        #Captura exceções do tipo 'IndexError' que são geradas quando se tenta acessar um indice inexistente
        except IndexError:
            print('Índice não existe na lista')
        #Captura as exceções que não foram tratadas pelos blocos 'excepet' anteriores
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')
        #Caso a lista for igual a 0, exibe que não há nada para listar
        if len(lista) == 0:
            print('Nada para listar')
        #Vai exibir os indices enumerados.
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')