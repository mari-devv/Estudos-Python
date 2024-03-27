#Primeiro, solicitamos ao usuário que insira um palpite para o número.
advinhe = int(input('Advinhe o número entre 1 e 10: '))
num_secreto = 8

#Em seguida, temos um loop while que continua enquanto o palpite do usuário for diferente do número secreto (neste caso, 8)
while num_secreto != advinhe:
#Se o palpite estiver incorreto, informamos ao usuário e solicitamos outro palpite
    print('Você errou. Tente novamente!')
    advinhe = int(input('Advinhe o número entre 1 e 10: '))
#Quando o usuário adivinha corretamente (quando advinhe é igual a num_secreto), o loop while termina e uma mensagem de parabéns é exibida.
print('Parabéns! Você acertou o número secreto 8!')