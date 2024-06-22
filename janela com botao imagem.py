from tkinter import*
def funcClicar ():
    print('botão pressionado')

janelaPrincipal=Tk()
texto = Label(master = janelaPrincipal, text = 'minha janela exibida')
texto.pack()
pic = PhotoImage(file='imagemteste.gif')
logo = Label(master = janelaPrincipal, image = pic)
logo.pack
botao = Button (master = janelaPrincipal, text = 'clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()
