#importar biblioteca
    #biblioteca tkinter serve para
from tkinter import *

#criar var tela
tela = Tk()

#titulo na barra de tarefas
tela.title("Fatec Registro")

#Configuração da cor da tela
tela.configure(background='#1e3743')

#configuração do tamanho da tela
tela.geometry("700x600")

#config max que a tela pode chegar
tela.resizable(True,True)
#tamanho max que a tela pode chegar
tela.maxsize(width=900, height=800)
#tamanho max que a tela pode chegar
tela.minsize(width=500, height=500)

#adicionar label
lbl_teste = label(tela, text="TESTE").place(x=10, y=10)

#lbl_teste é o nome de identificação interna da var
#label é o tipo de componente
#tela é a var que a label está ligada
#text="" é o texto a ser exibido na tela
#place é o posicionamento na tela

#comando mainloop serve para
tela.mainloop()

#F5 - atalho para depurar