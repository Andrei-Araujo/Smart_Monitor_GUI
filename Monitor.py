# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:25:08 2019

@author: Andrei
"""

users = {
    "111":"aaa",
    "222":"bbb",
    "333":"ccc",
    "444":"ddd"
}

admin = {
    "666":"kkk"
}

url = {
    "111":'http://www.sharecsv.com/dl/ced9e51ad803136e170d2ec2b8a2809f/Ocorrencias.csv',
    "222":'http://www.sharecsv.com/dl/cdbb54167641ffd1e954702b49a6cabf/Clarinda.csv',
    "333":'http://www.sharecsv.com/dl/fda5824bb506b58c7d3b31cf7540c634/Fernando.csv',
    "444":'http://www.sharecsv.com/dl/9ac3df6ff5cf5f5a1b82a9b86e2612b1/Bernardo.csv'
}

nomes = {
    "111":"Amarildo",
    "222":"Clarinda",
    "333":"Fernando",
    "444":"Bernardo",
}

import csv
import tkinter as tk
from urllib import request
from tkinter import *

LARGE_FONT = ("Verdana",12)



class Monitor(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        global w
        w= "a"
        print(w)

        global z
        z = 0


        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight =1)
        container.grid_columnconfigure(0, weight =1)

        self.frames = {}

        for F in (StartPage, PageUser, PageAdmin):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew") #nsew expande na direcao north-south e na direcao east-west



        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'Ocorrencias.csv'
    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\n")
    fx.close()




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global cpf
        cpf=5

        self.name = tk.IntVar()
        self.name2 = tk.IntVar()
        self.erro_lb = tk.StringVar()

        self.createWidgets()


        self.buttonAux2 = tk.Button(self, text="Verificar",
                            command=lambda:self.defAux())
        self.buttonAux2.pack(pady=10)

        self.buttonUser = tk.Button(self, text="Visit Page User",
                            command=lambda:controller.show_frame(PageUser))
        self.buttonUser.pack_forget()


        self.buttonAdmin = tk.Button(self, text="Prosseguir",
                            command=lambda:controller.show_frame(PageAdmin))
        self.buttonAdmin.pack_forget()


        #######################
    def defAux(self):
        # se for usuario
        global cpf
        cpf = self.nameEntered.get()
        if (self.nameEntered.get() in users and self.nameEntered2.get() == users.get(self.nameEntered.get())):
            self.buttonUser.pack(pady=10)
            self.buttonAux2.pack_forget()

            download_stock_data(url.get(self.nameEntered.get()))

            w= url.get(self.nameEntered.get())
            print(url.get(self.nameEntered.get()))
            z=50


        # se for admin
        elif (self.nameEntered.get() in admin and self.nameEntered2.get() == admin.get(self.nameEntered.get())):
            self.buttonAdmin.pack(pady=10)
            self.buttonAux2.pack_forget()
        # se nao for nada
        else:
            self.erro_lb.set("Senha Incorreta. Tente Novamente")

        ######################
    def createWidgets(self):
        #label PageName
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        #CPF LB (label)
        cpf_lb = tk.Label(self, text=" Digite seu CPF   ").pack(padx=5, pady=2)

        #CPF textbox
        name = tk.StringVar()
        self.nameEntered = tk.Entry(self, width=18, textvariable=name)
        self.nameEntered.pack( padx=30)

        #espacamento lb
        space_lb = tk.Label(self, text="").pack(pady=1)

        #senha lb
        senha_lb = tk.Label(self, text=" Senha   ").pack(padx=100)

        #senha Textbox
        name2 = tk.StringVar()
        self.nameEntered2 = tk.Entry(self, width=18, textvariable=name2)
        self.nameEntered2.pack( padx=30, pady=0)

        #espacamento lb
        space2_lb = tk.Label(self, text="", textvariable=self.erro_lb).pack(padx=2,pady=5)

class PageUser(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global w
        print("22")
        print(w)

        Start = []
        End = []
        Cuidador = []

        label = tk.Label(self, text="", font=LARGE_FONT)
        label.grid(pady=10,padx=10,row=0,column=0 )


        def ManipulaCSV(Start2, End2, Cuidador2):
            i=0
        # independente do usuario selecionado, o csv tera esse nome
            f = open('Ocorrencias.csv', 'r')
            file_contents = f.read()
            for row in file_contents:
                i=i+1

            f.close()

            #limpeza dos dados obtidos

            file_contents = file_contents[3:]
            file_contents = file_contents.replace('\n', ',' )
            file_contents = file_contents.replace('\\r', '' )

            file_contents = file_contents.split(",")

            file_contents.pop()
            print(file_contents)
            print(len(file_contents))
            print(file_contents[0])

            Print_Correto(file_contents, Start2, End2, Cuidador2)

        def Print_Correto (texto_errado, Start2, End2, Cuidador2):
            j=0
            k=0
            self.Start2=[]
            self.End2=[]
            self.Cuidador2=[]
            while j < len(texto_errado):
                if (j==0 or j%4==0):
                    j=j+1
                elif ((j-1)%4==0):
                    Start2.append(texto_errado[j])
                    j=j+1
                elif ((j-2)%4==0):
                    End2.append(texto_errado[j])
                    j=j+1
                else:
                    Cuidador2.append(texto_errado[j])
                    j=j+1

            while k < (len(Start2)):
                print(Start2[k])
                k=k+1

        def Show_Data ():
            ManipulaCSV(Start, End, Cuidador)
            print(Start, End, Cuidador)
            createWidgets2()
            buttonShow_Data.grid_remove()
            label.grid_remove()

        def createWidgets2():
            label_spacadora = tk.Label(self, text="Horarios das ocorrencias", font=LARGE_FONT)
            label_spacadora.grid(pady=5,padx=10,row=3,column=0 )

            label_Start = tk.Listbox(self)
            for n in range(len(Start)): label_Start.insert(END, Start[n])
            label_Start.grid(pady=10,padx=10,row=4,column=0)

            label_spacadora2 = tk.Label(self, text="Horarios das trocas", font=LARGE_FONT)
            label_spacadora2.grid(pady=5,padx=10,row=3,column=1 )

            label_End = tk.Listbox(self)
            for n in range(len(End)): label_End.insert(END, End[n])
            label_End.grid(pady=10,padx=10,row=4,column=1 )

            label_spacadora3 = tk.Label(self, text="Nomes dos cuidadores", font=LARGE_FONT)
            label_spacadora3.grid(pady=5,padx=10,row=3,column=2)

            label_Cuidador = tk.Listbox(self)
            for n in range(len(Cuidador)): label_Cuidador.insert(END, Cuidador[n])
            label_Cuidador.grid(pady=10,padx=10,row=4,column=2)

        buttonShow_Data = tk.Button(self, text="Mostrar Dados",
                            command=lambda: Show_Data() )
        buttonShow_Data.grid(row=0,column=1 )

class PageAdmin(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Selecione o paciente", font=LARGE_FONT)
        label.grid(pady=10,padx=10, row=0, column=0)

        buttonOne = tk.Button(self, text="Visualizar dados usuario",
                            command=lambda: controller.show_frame(PageUser) )
        buttonOne.grid(row=6,column=3, padx=10)

        buttonUser1 = tk.Button(self, text=nomes.get("111"), command=lambda: BtUser("111"))
        buttonUser1.grid(row=2,column=1)

        buttonUser2 = tk.Button(self, text=nomes.get("222"), command=lambda: BtUser("222"))
        buttonUser2.grid(row=2,column=2)

        buttonUser3 = tk.Button(self, text=nomes.get("333"), command=lambda: BtUser("333"))
        buttonUser3.grid(row=3,column=1)

        buttonUser4 = tk.Button(self, text=nomes.get("444"), command=lambda: BtUser("444"))
        buttonUser4.grid(row=3,column=2)

        label_invisivel = tk.Label(self, text="")
        label_invisivel.grid(pady=15,padx=10, row=5, column=2)

        def BtUser(number):
            download_stock_data(url.get(number))

app = Monitor()
app.mainloop()
