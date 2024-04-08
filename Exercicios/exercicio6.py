"""Jogo da palavra secreta"""

# Lista de palavras
palavras = ['amor', 'bola', 'gato']

# Escolho a palavra pelo indice
palavra_secreta = palavras[0]  

# Variáveis
letras_descobertas = ['_'] * len(palavra_secreta)
tentativas = 7
letras_usadas = []

# Loop principal do jogo
while tentativas > 0:
    # Mostra o estado atual da palavra
    for letra in letras_descobertas:
        print(letra, end=' ')
    print()
    
    # Pede ao usuário para adivinhar uma letra
    letra = input("Adivinhe uma letra: ").lower()
    
    # Verifica se a letra já foi usada
    if letra in letras_usadas:
        print("Você já tentou essa letra. Tente novamente.")
        continue
    
    letras_usadas.append(letra)
    
    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        print("Correto!")
        # Atualiza letras descobertas
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        print("Errado!")
        tentativas -= 1
    
    # Verifica se o jogador ganhou
    if '_' not in letras_descobertas:
        print("Parabéns, você ganhou! A palavra era:", palavra_secreta)
        break

# Se o jogador perdeu
if tentativas == 0:
    print("Você perdeu! A palavra secreta era:", palavra_secreta)
