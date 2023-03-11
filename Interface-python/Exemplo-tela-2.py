from tkinter import *

tela = Tk()
tela.title("Fatec Registro")

#dimensoes da janela do programa
largura = 800
altura =300

#resolução do S.O
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#visialização do tamanho da tela do terminal
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura,posx,posy))

tela.mainloop()