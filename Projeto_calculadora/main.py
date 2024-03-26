# Cria e importa as bibliotecas necessarias para dentro do script criado
# Importando o tkinter * = todos
from tkinter import *
from tkinter import ttk

#Criando a janela
janela = Tk()
#Definindo um nome para a janela
janela.title("Calculadora")
#Definindo largura e comprimento 1 valor para largura e o 2 para comprimento
janela.geometry("235x318")

#Dividindo as janelas
frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)


#mainloop vai permitir executarmos a janela
janela.mainloop()


