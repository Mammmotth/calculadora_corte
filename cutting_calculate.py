from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Canvas

root = Tk()


class Application:
    def __init__(self):
       self.root = root
       self.tela()
       self.frames_da_tela()
       self.frames_dos_blocos()
       self.bloco_input()
       self.titulo()
       self.subtitulos()
       self.inputs()      
       self.campos()
       self.botoes()
       self.tubos()
       
## Criando loop (mantem a tela aberta)   
       root.mainloop()

## Definições da janela
    def tela(self):
       self.root.title("Calculadora de Corte") #Titulo da Janela
       self.root.geometry("1366x800")
       self.root.configure(background="#dfe3ee")
       self.root.resizable(1,1)
       self.root.minsize(width=1024, height=768)
       self.root.maxsize(width=1480, height=900)

## Definições de quadrantes
    def frames_da_tela(self):
       self.frame_1 = Frame(self.root, bd=4, bg= "#f7f7f7", highlightbackground= "#8b9dc3", highlightthickness=2) ## Bloco de Configurações
       self.frame_1.place(relx=0.02, rely=0.1, relwidth=0.3, relheight=0.3)
       
       self.frame_2 = Frame(self.root, bd=4, bg="#f7f7f7", highlightbackground= "#8b9dc3", highlightthickness=2) ## Bloco de Corte
       self.frame_2.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.3)

       self.frame_3 = Frame(self.root, bd=4, bg="#f7f7f7", highlightbackground= "#8b9dc3", highlightthickness=2) ## Bloco de Estoque
       self.frame_3.place(relx=0.68, rely=0.1, relwidth=0.3, relheight=0.3)

       self.frame_tubos = Frame(self.root, bd=4, bg="#f7f7f7", highlightbackground= "#8b9dc3", highlightthickness=2) ## Quadrante dos tubos
       self.frame_tubos.place(relx=0.02, rely=0.415, relwidth=0.96, relheight=0.57)

##Definições dos titulos de cada quadrante
    def frames_dos_blocos(self):
       self.bloco_1 = Frame(self.frame_1, bd=0, bg="#8b9dc3", highlightbackground="#759fe6", highlightthickness=0)
       self.bloco_1.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)

       self.bloco_2 = Frame(self.frame_2, bd=0, bg="#8b9dc3", highlightbackground="#759fe6", highlightthickness=0)
       self.bloco_2.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)

       self.bloco_3 = Frame(self.frame_3, bd=0, bg="#8b9dc3", highlightbackground="#759fe6", highlightthickness=0)
       self.bloco_3.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.2)

## Definições para blocos que receberam informações do usuario    
    def bloco_input(self):
       self.label_corte = Text(self.frame_2, bd=0, bg="#ffffff", highlightbackground="#8b9dc3", highlightthickness=2,
                               font=("Verdana", 10, "italic"))
       self.label_corte.place(relx=0.52, rely=0.28, relwidth=0.45, relheight=0.58)
       
       self.label_estoque = Text(self.frame_3, bd=0, bg="#ffffff", highlightbackground="#8b9dc3", highlightthickness=2,
                               font=("Verdana", 10, "italic"))
       self.label_estoque.place(relx=0.52, rely=0.28, relwidth=0.45, relheight=0.58)

## Titulo que fica na janela do usuario
    def titulo(self):
      self.titulo = Label(self.root, text="Calculadora de Corte", foreground="#3b5998", background="#dfe3ee",
                           font=("Verdana", 28, "bold"))
      self.titulo.place(relx=0.34, rely=0.015)

## Titulo de cada quadrante   
    def subtitulos(self):
      self.subtitulo_1 = Label(self.bloco_1, text="Configurações", bg="#8b9dc3", foreground="#ffffff",
                                font=("Verdana", 18, "bold"))
      self.subtitulo_1.place(relx=0.25, rely=0.1)

      self.subtitulo_2 = Label(self.bloco_2, text="Corte", bg="#8b9dc3", foreground="#ffffff",
                               font=("Verdana", 18, "bold"))
      self.subtitulo_2.place(relx=0.4, rely=0.1)
      
      self.subtitulo_3 = Label(self.bloco_3, text="Estoque", bg="#8b9dc3", foreground="#ffffff",
                               font=("Verdana", 18, "bold"))
      self.subtitulo_3.place(relx=0.4, rely=0.1)
   
## Informativo para receber dados do usuario   
    def inputs(self):
       self.comprimento_configuracoes = Label(self.frame_1, text= "Comprimento:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.comprimento_configuracoes.place(relx=0.05, rely=0.30)
       
       self.quantidade_configuracoes = Label(self.frame_1, text= "Quantidade:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.quantidade_configuracoes.place(relx=0.05, rely=0.40)

       self.quantidade_configuracoes = Label(self.frame_1, text= "Corte:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.quantidade_configuracoes.place(relx=0.05, rely=0.50)

       self.comprimento_corte = Label(self.frame_2, text= "Comprimento:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.comprimento_corte.place(relx=0.05, rely=0.30)
       
       self.quantidade_corte = Label(self.frame_2, text= "Quantidade:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.quantidade_corte.place(relx=0.05, rely=0.40)

       self.comprimento_estoque = Label(self.frame_3, text= "Comprimento:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.comprimento_estoque.place(relx=0.05, rely=0.30)

       self.quantidade_estoque = Label(self.frame_3, text= "Quantidade:", bg="#f7f7f7", foreground="black",
                                              font=("Verdana", 10))
       self.quantidade_estoque.place(relx=0.05, rely=0.40)

## Campo para input de dados do usuario
    def campos(self):
       self.campos_comprimento_configuracoes = Entry(self.frame_1)
       self.campos_comprimento_configuracoes.place(relx=0.4, rely=0.31, relwidth=0.3)
       
       self.campos_quantidade_configuracoes = Entry(self.frame_1)
       self.campos_quantidade_configuracoes.place(relx=0.4, rely=0.41, relwidth=0.3)

       self.campos_corte_configuracoes = Entry(self.frame_1)
       self.campos_corte_configuracoes.place(relx=0.4, rely=0.51, relwidth=0.15)

       self.campos_comprimento_corte = Entry(self.frame_2)
       self.campos_comprimento_corte.place(relx=0.3, rely=0.31, relwidth=0.21)
       
       self.campos_quantidade_corte = Entry(self.frame_2)
       self.campos_quantidade_corte.place(relx=0.3, rely=0.41, relwidth=0.21)

       self.campos_comprimento_estoque = Entry(self.frame_3)
       self.campos_comprimento_estoque.place(relx=0.3, rely=0.31, relwidth=0.21)
       
       self.campos_quantidade_estoque = Entry(self.frame_3)
       self.campos_quantidade_estoque.place(relx=0.3, rely=0.41, relwidth=0.21)

## Dando função aos botes nos quadrantes 2(Corte) e 3(Estoque)
    def botoes(self):
       self.adicionar_corte = Button(self.frame_2, text="Adicionar", 
                                     font=("Verdana", 10, "bold"), command=self.transferir_corte)
       self.adicionar_corte.place(relx=0.30, rely=0.6, relwidth=0.2, relheight=0.2)

       self.limpar_corte = Button(self.frame_2, text="Clique para apagar", 
                                  font=("Verdana", 8, "bold italic"), command=self.apagar_corte)
       self.limpar_corte.place(relx=0.58, rely=0.89)

       self.adicionar_estoque = Button(self.frame_3, text="Adicionar",
                                     font=("Verdana", 10, "bold"), command=self.transferir_estoque)
       self.adicionar_estoque.place(relx=0.30, rely=0.6, relwidth=0.2, relheight=0.2)

       self.limpar_estoque = Button(self.frame_3, text="Clique para apagar",
                                  font=("Verdana", 8, "bold italic"), command=self.apagar_estoque)
       self.limpar_estoque.place(relx=0.58, rely=0.89)

    def transferir_corte(self):
      
      self.entry_comprimento_corte = self.campos_comprimento_corte.get()
      self.entry_quantidade_corte = self.campos_quantidade_corte.get()
      
      self.campos_comprimento_corte.delete(0, END)
      self.campos_quantidade_corte.delete(0, END)
      
      self.label_corte.insert(END, f"{self.entry_comprimento_corte} x {self.entry_quantidade_corte} \n")
        
    def apagar_corte(self):
       self.label_corte.delete("1.0", "end")

    def transferir_estoque(self):
      
       self.entry_comprimento_estoque = self.campos_comprimento_estoque.get()
       self.entry_quantidade_estoque = self.campos_quantidade_estoque.get()
      
       self.campos_comprimento_estoque.delete(0, END)
       self.campos_quantidade_estoque.delete(0, END)
      
       self.label_estoque.insert(END, f"{self.entry_comprimento_estoque} x {self.entry_quantidade_estoque} \n")
    
    def apagar_estoque(self):
       self.label_estoque.delete("1.0", "end")

#
    def tubos(self):
        self.tubo_1 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_1.place(relx=0.01, rely=0.02, relwidth=0.04, relheight=0.965)
        
        self.tubo_2 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_2.place(relx=0.06, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_3 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_3.place(relx=0.11, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_4 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_4.place(relx=0.16, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_5 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_5.place(relx=0.21, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_6 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_6.place(relx=0.26, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_7 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_7.place(relx=0.31, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_8 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_8.place(relx=0.36, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_9 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_9.place(relx=0.41, rely=0.02, relwidth=0.04, relheight=0.965) 

        self.tubo_10 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_10.place(relx=0.46, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_11 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_11.place(relx=0.51, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_12 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_12.place(relx=0.56, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_13 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_13.place(relx=0.61, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_14 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_14.place(relx=0.66, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_15 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_15.place(relx=0.71, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_16 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_16.place(relx=0.76, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_17 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_17.place(relx=0.81, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_18 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_18.place(relx=0.86, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_19 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_19.place(relx=0.91, rely=0.02, relwidth=0.04, relheight=0.965)

        self.tubo_20 = Canvas(self.frame_tubos, bd=2, bg= "#8b9dc3", highlightbackground="#8b9dc3", highlightthickness=1)
        self.tubo_20.place(relx=0.96, rely=0.02, relwidth=0.04, relheight=0.965)


Application()
