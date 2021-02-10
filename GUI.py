from tkinter import *

#corpo do programa
janela = Tk()
janela.title("Destruir.exe")
janela.geometry('300x200+0+0')
#--

#definições
    #definição da ação que o botão1 vai fazer ao ser pressionado
def botao_pressionado():
    import imp
    pasta_digitada = e1.get()
    imp.destruir_pasta(pasta_digitada)

def botao2_pressionado():
    exit()
#--

#botão
    #botão1 = ação
        #especificações do botão1, coordenadas, texto e ação
b1 = Button(janela, text="DESTRUIR", command = botao_pressionado)
b1.place(x=110, y=80)

    #botão2 = sair
        #sai do programa
b2 = Button(janela, text="SAIR", command = botao2_pressionado)
b2.pack(anchor = W)
b2.place(x=130, y=110)
#--

#campo de escrita/entrada de informação
    #usuário fornece a informação
e1 = Entry(janela)
e1.pack(side=TOP)
e1.place(x=50, y=50)
#--

#texto
    #"instruções"
#Label(janela,text='Caminho da Pasta :', font=fonte1,width=8).pack(side=LEFT)
#e1 = e1.label(janela, text="Hello Tkinter!")
Label(janela,text='Cole o Caminho da Pasta abaixo :').place(x=40, y=20)
#Label.place(x=50, y=20)
#--

janela.mainloop()
