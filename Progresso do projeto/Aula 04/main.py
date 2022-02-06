from tkinter import *
from customer_registration.style import config


class Application:
    def __init__(self):
        # Criação da janela principal
        self.main_window = Tk()

        # Invocando funções
        self.screen()
        self.frames_screen()
        self.first_frame_widgets()

        # Colocando o app em loop
        self.main_window.mainloop()

    def screen(self):
        # Criando as configurações da janela principal
        self.main_window.title('Cadastro de clientes')
        self.main_window.configure(bg=config['cor1'])
        self.main_window.geometry('700x500')
        self.main_window.resizable(True, True)
        self.main_window.maxsize(width=900, height=700)
        self.main_window.minsize(width=500, height=400)

    def frames_screen(self):
        # Criação dos 2 frames principais
        self.firstFrame = Frame(self.main_window, bd=4, bg=config['cor2'], highlightbackground=config['cor3'],
                                highlightthickness=3)
        self.secondFrame = Frame(self.main_window, bd=4, bg=config['cor2'], highlightbackground=config['cor3'],
                                 highlightthickness=3)

        # Posicionado os 2 frames principais
        self.firstFrame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.secondFrame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def first_frame_widgets(self):
        # Criando os botões do primeiro frame
        self.btn_clear = Button(self.firstFrame, text='Limpar', bd=3, bg=config['cor4'], fg='white',
                                font=config['font'])
        self.btn_search = Button(self.firstFrame, text='Buscar', bd=3, bg=config['cor4'], fg='white',
                                font=config['font'])
        self.btn_new = Button(self.firstFrame, text='Novo', bd=3, bg=config['cor4'], fg='white',
                                 font=config['font'])
        self.btn_change = Button(self.firstFrame, text='Mudar', bd=3, bg=config['cor4'], fg='white',
                                 font=config['font'])
        self.btn_delete = Button(self.firstFrame, text='Deletar', bd=3, bg=config['cor4'], fg='white',
                                 font=config['font'])

        # Posicionando os botões do primeiro frame
        self.btn_clear.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn_search.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn_new.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn_change.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btn_delete.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criando as labels do primeiro frame
        self.label_code = Label(self.firstFrame, text='Código', bg=config['cor2'], fg=config['cor4'],
                                font=config['font'])
        self.label_name = Label(self.firstFrame, text='Nome', bg=config['cor2'], fg=config['cor4'],
                                font=config['font'])
        self.label_telephone = Label(self.firstFrame, text='Telefone', bg=config['cor2'], fg=config['cor4'],
                                font=config['font'])
        self.label_city = Label(self.firstFrame, text='Cidade', bg=config['cor2'], fg=config['cor4'],
                                font=config['font'])

        # Posicionando os labels do primeiro frame
        self.label_code.place(relx=0.05, rely=0.05)
        self.label_name.place(relx=0.05, rely=0.35)
        self.label_telephone.place(relx=0.05, rely=0.6)
        self.label_city.place(relx=0.4, rely=0.6)

        # Criando os entry do primeiro frame
        self.entry_code = Entry(self.firstFrame)
        self.entry_name = Entry(self.firstFrame)
        self.entry_telephone = Entry(self.firstFrame)
        self.entry_city = Entry(self.firstFrame)

        # Posicionando os entry do primeiro frame
        self.entry_code.place(relx=0.05, rely=0.15, relwidth=0.1, relheight=0.1)
        self.entry_name.place(relx=0.05, rely=0.45, relwidth=0.75, relheight=0.1)
        self.entry_telephone.place(relx=0.05, rely=0.7, relwidth=0.2, relheight=0.1)
        self.entry_city.place(relx=0.4, rely=0.7, relwidth=0.4, relheight=0.1)


Application()
