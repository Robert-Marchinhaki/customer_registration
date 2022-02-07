from tkinter import *
from customer_registration.style import config
from tkinter import ttk
import sqlite3


class Funcs:
    def clear_screen(self):
        self.entry_code.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_telephone.delete(0, END)
        self.entry_city.delete(0, END)

    def connect_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
        print('Conectando ao banco de dados')

    def disconnect_bd(self):
        self.conn.close()
        print('Desconectando do banco de dados')

    def create_table(self):
        self.connect_bd()

        # Criando tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit()
        print('Banco de dados criado')
        self.disconnect_bd()

    def variables(self):
        self.code = self.entry_code.get()
        self.name = self.entry_name.get()
        self.telephone = self.entry_telephone.get()
        self.city = self.entry_city.get()

    def add_client(self):
        self.variables()
        self.connect_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?) """, (self.name, self.telephone, self.city))

        self.conn.commit()
        self.disconnect_bd()
        self.select_list()
        self.clear_screen()

    def select_list(self):
        self.customer_list.delete(*self.customer_list.get_children())
        self.connect_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.customer_list.insert("", END, values=i)
        self.disconnect_bd()

    def on_double_click(self, event):
        self.clear_screen()
        self.customer_list.selection()

        for n in self.customer_list.selection():
            col1, col2, col3, col4 = self.customer_list.item(n, 'values')
            self.entry_code.insert(END, col1)
            self.entry_name.insert(END, col2)
            self.entry_telephone.insert(END, col3)
            self.entry_city.insert(END, col4)

    def delete_client(self):
        self.variables()
        self.connect_bd()

        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", (self.code))
        self.conn.commit()

        self.disconnect_bd()
        self.clear_screen()
        self.select_list()


class Application(Funcs):
    def __init__(self):
        # Criação da janela principal
        self.main_window = Tk()

        # Invocando funções
        self.screen()
        self.frames_screen()
        self.first_frame_widgets()
        self.second_frame_list()
        self.create_table()
        self.select_list()

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
                                font=config['font'], command=self.clear_screen)
        self.btn_search = Button(self.firstFrame, text='Buscar', bd=3, bg=config['cor4'], fg='white',
                                font=config['font'])
        self.btn_new = Button(self.firstFrame, text='Novo', bd=3, bg=config['cor4'], fg='white',
                                 font=config['font'], command=self.add_client)
        self.btn_change = Button(self.firstFrame, text='Mudar', bd=3, bg=config['cor4'], fg='white',
                                 font=config['font'])
        self.btn_delete = Button(self.firstFrame, text='Deletar', bd=3, bg=config['cor4'], fg='white',
                                 font=config['font'], command=self.delete_client)

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

    def second_frame_list(self):
        self.customer_list = ttk.Treeview(self.secondFrame, height=3, columns=('col1', 'col2', 'col3', 'col4'))

        # Nomeando as colunas da lista
        self.customer_list.heading('#0', text='')
        self.customer_list.heading('#1', text='Código')
        self.customer_list.heading('#2', text='Nome')
        self.customer_list.heading('#3', text='Telefone')
        self.customer_list.heading('#4', text='Cidade')

        # Width de 500 (dividido entre 4 itens)
        self.customer_list.column('#0', width=1)
        self.customer_list.column('#1', width=50)
        self.customer_list.column('#2', width=200)
        self.customer_list.column('#3', width=125)
        self.customer_list.column('#4', width=100)

        # Ajustando a posição da lista
        self.customer_list.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Criando a Scrollbar da lista
        self.scrool_list = Scrollbar(self.secondFrame, orient='vertical')
        self.customer_list.configure(yscroll=self.scrool_list.set)
        self.scrool_list.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)
        self.customer_list.bind("<Double-1>", self.on_double_click)



Application()
