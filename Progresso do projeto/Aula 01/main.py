from tkinter import *


class Application:
    def __init__(self):
        # Criação da janela principal
        self.main_window = Tk()

        # Invocando funções
        self.screen()

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


Application()
