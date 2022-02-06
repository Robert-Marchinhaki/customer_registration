from tkinter import *


class Application:
    def __init__(self):
        # Criação da janela principal
        self.main_window = Tk()

        # Invocando funções
        self.screen()
        self.frames_screen()

        # Colocnado o app em loop
        self.main_window.mainloop()

    def screen(self):
        # Criando as configurações da janela principal
        self.main_window.title('Cadastro de clientes')
        self.main_window.configure(bg='#1e3743')
        self.main_window.geometry('700x500')
        self.main_window.resizable(True, True)
        self.main_window.maxsize(width=900, height=700)
        self.main_window.minsize(width=500, height=400)

    def frames_screen(self):
        # Criação dos 2 frames principais
        self.firstFrame = Frame(self.main_window, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',
                                highlightthickness=3)
        self.secondFrame = Frame(self.main_window, bd=4, bg='#dfe3ee', highlightbackground='#759fe6',
                                 highlightthickness=3)

        # Posicionado os 2 frames principais
        self.firstFrame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.secondFrame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)


Application()
