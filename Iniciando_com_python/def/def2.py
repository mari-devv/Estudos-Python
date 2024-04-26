"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
"""
O escopo se refere a visibilidade e acessibilidade das variáveis em diferentes partes do código.
Ele é determinado principalmente pelo local onde elas são definidas, e as funções desempenham um papel importante nisso.
"""

"""
Quando você define uma variável dentro de uma função, ela geralmente tem um escopo local, o que significa que só pode ser acessada dentro dessa função.
Isso significa que a variável só existe enquanto a função estiver sendo executada e desaparece quando a função termina. Por exemplo:
"""
def minha_funcao():
    x = 10  #Esta é uma variável local
    print(x)

minha_funcao()  # Isso imprimirá 10
print(x)  # Isso resultará em um erro, porque x não está definido aqui fora da função

"""No entanto, você também pode acessar variáveis fora da função, mas dentro da qual ela está definida. Essas variáveis têm um escopo global. Por exemplo:"""

y = 20  # Esta é uma variável global

def minha_funcao():
    print(y)  # Esta função pode acessar a variável global y

minha_funcao()  # Isso imprimirá 20

"""Se você definir uma variável com o mesmo nome dentro de uma função, essa variável terá um escopo local e não afetará a variável global com o mesmo nome. Por exemplo:"""

z = 30  # Variável global

def minha_funcao():
    z = 40  # Variável local com o mesmo nome
    print(z)  # Isso imprimirá 40

minha_funcao()
print(z)  # Isso imprimirá 30, pois a variável global não foi afetada

