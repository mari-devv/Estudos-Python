"""Jogo da palavra secreta"""

palavra = input('Insira a palavra secreta: ').lower()  # Converte a palavra inserida para minúsculas
palavra_secreta = 'amor'

if palavra != palavra_secreta:
    print('Você errou a palavra')
else:
    print('Você acertou a palavra')
