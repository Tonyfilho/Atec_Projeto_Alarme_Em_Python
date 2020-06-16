'''
Sistema de Alarme, do Projeto Final de Python do Professor Luis da Atec Palmela.

@autor : Tony E Debora
@Data  : 05-15-2020
@Linguagem : Python

'''

# +++++++++++++++++++++++++++++++++++++++++++
# Bibliotecas
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import tkinter as tk
import csv
from PIL import ImageTk, Image
from time import sleep


# +++++++++++++++++++++++++++++++++++++++++++
# dados Globais


Int_img = ['Botao_Off1_d.png', 'Botao_On1_d.png']
estado1, estado2 = False, False

dados = [];
# +++++++++++++++++++++++++++++++++++++++++++
# Metodos
def donothing():
    pass


# ++++++++++++++++++++++++++++++++
def ler_ficheiro():
    i = 0
    f = open('alarmes.dat', 'r')
    linha = f.readline()
    print('{} : {}'.format(i, linha))
    while linha != '':
        i += 1
        linha = f.readline()
        print('{} : {}'.format(i, linha))


# ++++++++++++++++++++++++++++++++
def Autor():
    messagebox.showinfo('Dialogo Autor',
                        '\nName : Antonio Filho & Debora Mutiz\nFunction : It Trainning\nCurso: CET´s Palmela\n\nMake the thing\'s easy')


# ++++++++++++++++++++++++++++++++
def Linguagem():
    messagebox.showinfo('Dialogo Linguagem',
                        '\nLanguage : Python\nVersion : 3.80 ')


# ++++++++++++++++++++++++++++++++
def Programa():
    messagebox.showinfo('Dialogo Programa',
                        '\nPrograma que mostra\numa interface de um Alarme\nnuma aplicação Python GUI(Tkinter)')


# ++++++++++++++++++++++++++++++++
def abandonar():
    perg = messagebox.askquestion('Dialogo Abandonar',
                                  '\nConfirma que deseja\nabandonar a aplicação.\n')
    if perg == 'yes':
        root.destroy()


# ++++++++++++++++++++++++++++++++
def AlarmePortas():
    global estado1
    global bt1
    global imag1

    estado1 = not (estado1)

    if estado1 == True:
        # string da caixa de texto
        ms1.set('ON')

        # Imagem do interruptor
        imag1 = PhotoImage(file=Int_img[1])
        b1.configure(image=imag1)

        # cor do led
        c.itemconfig(porta1Res, fill='red')
        c.itemconfig(porta1Pri, fill='red')

        # captura dia, data, hora
        hoje = datetime.now()
        data = hoje.strftime("%d-%m-%Y")
        horas = hoje.strftime("%H:%M")

        # abrir o ficheiro para adicionar dados
        arquivo = open('alarmes.dat', 'a')

        # escreve os dados por linha
        arquivo.write(' Alarme Acionado nas Portas ')
        arquivo.write(',')
        arquivo.write(data)
        arquivo.write(',')
        arquivo.write(horas)
        arquivo.write('\n')

        # fechar o ficheiro
        arquivo.close()
    else:
        ms1.set('OFF')
        imag1 = PhotoImage(file=Int_img[0])
        b1.configure(image=imag1)
        c.itemconfig(porta1Res, fill='orange')
        c.itemconfig(porta1Pri, fill='orange')



# ++++++++++++++++++++++++++++++++
def AlarmeJanelas():
    global estado2
    global bt2
    global imag2

    estado2 = not (estado2)

    if estado2 == True:
        # string da caixa de texto
        ms2.set('ON')

        # Imagem do interruptor
        imag2 = PhotoImage(file=Int_img[1])
        b2.configure(image=imag2)

        # cor do led
        c.itemconfig(janela1Res, fill='red')
        c.itemconfig(janela2Res, fill='red')
        c.itemconfig(janela3Res, fill='red')
        c.itemconfig(janela4Res, fill='red')
        c.itemconfig(janela5Res, fill='red')
        c.itemconfig(janela6Res, fill='red')
        c.itemconfig(janela1Pri, fill="red")
        c.itemconfig(janela2Pri, fill="red")
        c.itemconfig(janela3Pri, fill="red")
        c.itemconfig(janela4Pri, fill="red")
        c.itemconfig(janela5Pri, fill="red")
        c.itemconfig(janela6Pri, fill="red")

        # captura dia, data, hora
        hoje = datetime.now()
        data = hoje.strftime("%d-%m-%Y")
        horas = hoje.strftime("%H:%M")

        # abrir o ficheiro para adicionar dados
        arquivo = open('alarmes.dat', 'a')

        # escreve os dados por linha
        arquivo.write(' Alarme Acionado nas Janelas ')
        arquivo.write(',')
        arquivo.write(data)
        arquivo.write(',')
        arquivo.write(horas)
        arquivo.write('\n')

        # fechar o ficheiro
        arquivo.close()
    else:
        ms2.set('OFF')
        imag2 = PhotoImage(file=Int_img[0])
        b2.configure(image=imag2)
        c.itemconfig(janela1Res, fill='orange')
        c.itemconfig(janela2Res, fill='orange')
        c.itemconfig(janela3Res, fill='orange')
        c.itemconfig(janela4Res, fill='orange')
        c.itemconfig(janela5Res, fill='orange')
        c.itemconfig(janela6Res, fill='orange')
        c.itemconfig(janela1Pri, fill="orange")
        c.itemconfig(janela2Pri, fill="orange")
        c.itemconfig(janela3Pri, fill="orange")
        c.itemconfig(janela4Pri, fill="orange")
        c.itemconfig(janela5Pri, fill="orange")
        c.itemconfig(janela6Pri, fill="orange")
#*******************************************************Funções de troca de IMG na TAB0
def next(panel):
    #quant = 0
    imagens = ["piso_um.png", "pisonovozero1.png", "piso_zero.png", "pisonovozero.png"]
    for i in imagens:
       path = i


    #path = "pisonovozero.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!

def prev(panel):

    path = "casa2_imagem.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel.configure(image=img)
    panel.image = img # keep a reference!





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++Show
def show():
    lista = []  # você só precisa de uma lista - ela é uma matriz multidimensional

    with open('alarmes.dat', newline='') as csvfile:
        separador = csv.reader(csvfile, delimiter=',')  # separe por vírgula
        # o módulo csv detectará novas linhas automaticamente
        for i in separador:
            lista.append(i)

    print(lista[1])  # imprime a linha 2 da lista, inteira
    for i in lista:
        Data = i[2]
        Hora = i[0]
        Sensor = i[1]
        listBox.insert("", "end", values=(i, Sensor, Data, Hora))

# +++++++++++++++++++++++++++++++++++++++++++
# GUI
root = Tk()
root.title("Alarme Atec")  # -------------------------------------Titulo
root.geometry("1000x700")  # -------------------------------------Dimensão total da TELA
root.resizable(True, True)  # ---------------------------------- redimensionavel

# +++++++++++++++++++++++++++++++++++++++++++
# MenuBar
menubar = Menu()

# +++++++++++++++++++++++++++++++++++++++++++
# Menu
filemenu = Menu(menubar, tearoff=0)

# +++++++++++++++++++++++++++++++++++++++++++
# MenuItem
filemenu.add_command(label='Ler ficheiro', command=ler_ficheiro)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=abandonar)

# Titulo do Menu
menubar.add_cascade(label='File', menu=filemenu)

# Menu filehlp
filehlp = Menu(menubar, tearoff=0)

# MenuItem
filehlp.add_command(label='Programa', command=Programa)
filehlp.add_command(label='Linguagem', command=Linguagem)
filehlp.add_separator()
filehlp.add_command(label='Autor', command=Autor)

# Titulo do Menu
menubar.add_cascade(label='Help', menu=filehlp)

# juntar o menu a root
root.config(menu=menubar)

# juntar o menu a root
root.config(menu=menubar)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Notebook
note = ttk.Notebook(root)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab0 ----------------------------------------------------------------imagem da capa
tab0 = Frame(note)

#imagemCapa = PhotoImage(file='casa2_imagem.png')
#lb_capa = Label(tab0, image=imagemCapa)
#lb_capa.pack(side=LEFT, pady=10)


#Create main window
window = tab0

#divide window into two sections. One for image. One for buttons
top = tk.Frame(window)
top.pack(side="top")
bottom = tk.Frame(window)
bottom.pack(side="bottom")

#place image
path = "casa2_imagem.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.image = img # keep a reference!
panel.pack(side = "top", fill = "both", expand = "yes")

#place buttons
prev_button = tk.Button(window, text="Inicio", width=10, height=2, bg="black", fg="red", command=lambda: prev(panel))
prev_button.pack(in_=bottom, side="left")
next_button = tk.Button(window, text="Proxima", width=10, height=2,bg="red", fg="black", command=lambda: next(panel))
next_button.pack(in_=bottom, side="right")

#Start the GUI
#window.mainloop()














#************************************************************************* fim do TAB0
# tab 1
tab1 = Frame(note)
# +++++++++++++++++++++++++++++++++++++++++++
# painel superior--------------------------------------1ºpainel da planta abitação
p1 = Frame(tab1, width="1200", height="40", bg="black")

# Label
lb1 = Label(p1, text="Portas", fg="blue")
lb1.pack(side=LEFT, padx=20, pady=20)

# Caixa de Texto
ms1 = StringVar()
E1 = Entry(p1, textvariable=ms1)
E1.insert(END, 'OFF')
E1.pack(side=LEFT, padx=20, pady=20)

# Label
lb2 = Label(p1, text="Janelas", fg="blue")
lb2.pack(side=LEFT, padx=20, pady=20)

# caixa de texto
ms2 = StringVar()
E2 = Entry(p1, textvariable=ms2)
E2.insert(END, 'OFF')
E2.pack(side=LEFT, padx=20, pady=20)

# adicionar o painel
p1.pack()

# +++++++++++++++++++++++++++++++++++++++++++
# --------------------------------------------------------------------painel grafico01
c = Canvas(tab1, width="1200", height="550", bg="white")

# sem alarme
img_ps0 = PhotoImage(file='pisonovozero.png')  # imagem de fundo planta
fundo = c.create_image(20, 275, image=img_ps0, anchor=W)#--------------------------ALTERADO
porta1Res = c.create_oval(70, 120, 80, 130, fill='orange')  # -----------------------------Alarme
janela1Res = c.create_oval(70, 450, 80, 460, fill='orange')  # -----------------------------Alarme_janela
janela2Res = c.create_oval(200, 450, 210, 460, fill='orange')  # -----------------------------Alarme_janela
janela3Res = c.create_oval(330, 450, 340, 460, fill='orange')  # -----------------------------Alarme_janela
janela4Res = c.create_oval(290, 120, 300, 130, fill='orange')  # -----------------------------Alarme_janela
janela5Res = c.create_oval(350, 180, 360, 190, fill='orange')  # -----------------------------Alarme_janela
janela6Res = c.create_oval(510, 210, 520, 220, fill='orange')  # -----------------------------Alarme_janela




# sem alarme

#c.pack()

#---------------------------------------------------painel grafico02
# sem alarme
img_ps1 = PhotoImage(file='pisonovozero.png')  # imagem de fundo planta
fundo = c.create_image(620, 275, image=img_ps0, anchor=W)#--------------------------ALTERADO
porta1Pri = c.create_oval(670, 120, 680, 130, fill='orange')  # --------------------------------Alarme Portas
# sem alarme
janela1Pri = c.create_oval(680, 450, 690, 460, fill='orange')  # # --------------------------------Alarme janela
janela2Pri = c.create_oval(820, 450, 830, 460, fill='orange')  # -----------------------------Alarme_janela
janela3Pri = c.create_oval(920, 450, 930, 460, fill='orange')  # -----------------------------Alarme_janela
janela4Pri = c.create_oval(1110, 220, 1120, 230, fill='orange')  # -----------------------------Alarme_janela
janela5Pri = c.create_oval(1180, 820, 1190, 830, fill='blue')  # -----------------------------Alarme_janela
janela6Pri = c.create_oval(1180, 680, 1190, 690, fill='blue')  # -----------------------------Alarme_janela




c.pack()# +++++++++++++++++++++++++++++++++++++++++++




# -----------------------------------------------------------------------painel inferior
p2 = Frame(tab1, width="1200", height="80", bg="black")

# Imagem
img1 = PhotoImage(file=Int_img[0])

# Button
b1 = Button(p2, image=img1, command=AlarmePortas)  # text="AlarmePortas OFF"
b1.pack(side=LEFT, padx=80, pady=20)

# imagem
img2 = PhotoImage(file=Int_img[0])

# Button
b2 = Button(p2, image=img2, command=AlarmeJanelas)  # text="AlarmeJanelas ON"
b2.pack(side=LEFT, padx=100, pady=20)

# adicionar o painel
p2.pack()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# tab 2-----------------------------------------------------------------Registro de Ocorrências
tab2 = Frame(note)
p3 = Frame(tab2, width="1000", height="200", bg="")
#tabela = Label(p3, command=ler_ficheiro())

#----------------------------------------------------------------------------fim do teste
p3.pack()#------------------------------------------------------------fim do p3.tab2
#-------------------------------------------------------------------inicio do C.canvas.Tab02
d = Canvas(tab2, width="1200", height="550", bg="black")
label = tk.Label(d, text="Tabela de Eventos de Alarme", font=("Arial", 20)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('Local do Alarme', 'Data', 'Hora')
listBox = ttk.Treeview(d, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)
showScores = tk.Button(d, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(d, text="Close", width=15, command=exit).grid(row=4, column=1)


d.pack()
# Imagem da bola
img3 = PhotoImage(file='redball.gif')

# Titulo dos separadores
note.add(tab0, text='  Capa da App  ', image=img3, compound=LEFT)
note.add(tab1, text='  Planta da Habitação  ', image=img3, compound=LEFT)
note.add(tab2, text='  Registo de ocorrencias  ', image=img3, compound=LEFT)

note.pack(expand=1, fill=BOTH)

# +++++++++++++++++++++++++++++++++++++++++++
# mostrar o GUI
root.mainloop()

