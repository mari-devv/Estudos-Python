"""
Introdução as funções (def) em Python
Funções são trechos de códigos usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros(argumentos), e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

"""def imprimir(a, b ,c):
    print('Várias')
    print('Várias 1') 
    print('Várias 2')  

imprimir(1, 2, 3)
"""
"""
Uma função em python é um bloco de código reutilizável que executa uma tarefa específica.
O uso de funções ajuda na organização de código, tornando-o mais legível.

Ao usar 'def', você define o nome da função seguido por parênteses que podem conter argumentos necessários para a função.
Estes argumentos são variáveis que a função pode usar para realizar sua tarefa.
"""

def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)
resultado2 = soma(45, 30)
print(resultado2)
