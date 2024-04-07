from tkinter import*
from PIL import*
from PIL import Image,ImageTk
from random import*
from math import*
import math
import os
#Configuration de la fenêtre
fen=Tk()
fen.title("julworks")
fen.geometry("390x650")
fen.minsize(480, 360)
frame = Frame(fen, bg='#FFFFFF', bd=1, relief=SUNKEN)

#frame 1, bords de la calculatrice

Frame1 = Frame(fen, borderwidth=1 , highlightbackground="red",highlightthickness=2)
Frame1.pack(side=LEFT, padx=10, pady=10)
Label(Frame1, text="").pack(padx=234, pady=312)
Label(Frame1, text="JULWORKS", font=("Courrier", 13), fg="orange").place(x=170, y=0)

#Frame 3 des boutons de la calculatrice
Frame3 = Frame(fen, borderwidth=1 , highlightbackground="black",highlightthickness=2)
Frame3.place(x = 38, y = 400)

#frame 4 des boutons de déplacements
Frame4 = Frame(fen, borderwidth=1 , highlightbackground="black",highlightthickness=2)
Frame4.place(x = 38, y = 300)
historique=0

#les écrans
#écran de calcul
Ecran = Entry(fen, fg="black", font=("Courrier",28,'bold'), bg="grey", width="20")
Ecran.place(x = 30, y = 120)
#écran de l'historique des résultats
Ecran1 = Entry(fen, fg="white", font=("Courrier",20,'bold'), bg="black", width="20")
Ecran1.place(x = 30, y = 77)

    
#Les fonctions

global operateur

#bouton quand on clique sur une touche d'opération et de chiffre
def bouton_click(nbre):#affiche les nombres tapés
    
    operateur=""
    operateur=operateur+str(nbre)
    Ecran.insert(10,operateur)

#fonction qui efface l'ecran de calcul et l'écran d'historique
def bouton_clear():#nettoie l'écran
    historique=Ecran.get()
    Ecran1.delete(0,10000)
    Ecran.delete(0,10000)
    Ecran1.insert(10,(historique))

    return historique
#fonction qui efface la dernière valeur de l'écran d'historique
def bouton_supp():
    Ecran.delete(0,1)

#fonction qui affiche le résultat
def bouton_egal():
    calcul=Ecran.get()
    try:
        result = eval(calcul)
        Ecran.delete(0, 100000)
        Ecran.insert(100000, result)
    except Exception:
        Ecran.delete(0, 100000)
        Ecran.insert(10, "Error")

def bouton_off():
    fen.destroy()

#les fonctions de sin, cos et tan

def bouton_sin():

    sin1=math.sin(math.radians(float(Ecran.get())))
    Ecran.delete(0,100000)
    Ecran.insert(10,(sin1))
def bouton_cos():

    sin1=math.cos(math.radians(float(Ecran.get())))
    Ecran.delete(0,100000)
    Ecran.insert(10,(sin1))
def bouton_tan():

    sin1=math.tan(math.radians(float(Ecran.get())))
    Ecran.delete(0,100000)
    Ecran.insert(10,(sin1))

#fonctions pour déplacer le curseur

def shift_cursor1(event=None):
    position = Ecran.index(INSERT)
    Ecran.icursor(position - 1)

def shift_cursor2(event=None):
    position = Ecran.index(INSERT)
    Ecran.icursor(position + 1)

def shift_cursor3():
    historique = Ecran1.get()
    Ecran.delete(0, END)
    Ecran.insert(0, historique)

photo = PhotoImage(file = r"on.png")
# Ajouter l'image dans le bouton 
Button(fen, image=photo, width=30, height=30, command=lambda:bouton_off()).place(x = 220, y = 348)

photo1 = PhotoImage(file = r"home.png")
# Ajouter l'image dans le bouton 
Button(fen, image=photo1, width=30, height=30).place(x = 220, y = 298)

photo2 = PhotoImage(file = r"ok.png")
# Ajouter l'image dans le bouton 
Button(fen, image=photo2, width=40, height=40, command=lambda:bouton_egal()).place(x = 300, y = 320)

photo3 = PhotoImage(file = r"fleche.png")
# Ajouter l'image dans le bouton 
Button(fen, image=photo3, width=40, height=40).place(x = 400, y = 320)
#boutons pour déplacer le curseur

haut= Button(Frame4, text='▲', width =6, fg="orange", activebackground='yellow', bg='#FFF4C0', command=shift_cursor3).grid(row =1, column =1)
gauche= Button(Frame4, text='◄', width =6, fg="orange", activebackground='yellow', bg='#FFF4C0', command=shift_cursor1).grid(row =2, column =0)
bas=Button(Frame4, text='▼', width =6, fg="orange", activebackground='yellow', bg='#FFF4C0').grid(row =3, column =1)
droit=Button(Frame4, text='►', width =6, fg="orange", activebackground='yellow', bg='#FFF4C0', command=shift_cursor2).grid(row =2, column =2)



#Les boutons de la calculatrice

clear= Button(Frame3, text='Clear', width =13, borderwidth=3,fg="orange", activebackground='yellow', command=lambda:bouton_clear()).grid(row =2, column =0)
annuler= Button(Frame3, text='supp →', width =13, fg="orange", activebackground='yellow', command=lambda:bouton_supp()).grid(row =2, column =1)
xcarre= Button(Frame3, text='x²', width =13, fg="orange", activebackground='yellow', command=lambda:bouton_click("**2")).grid(row =2, column =2)
xy= Button(Frame3, text='xʸ', width =13, fg="orange", activebackground='yellow', command=lambda:bouton_click("**")).grid(row =2, column =3)
sin= Button(Frame3, text='sin', width =13, command=lambda:bouton_sin()).grid(row =3, column =0)
cos=Button(Frame3, text='cos', width =13, command=lambda:bouton_cos()).grid(row =3, column =1)
tan=Button(Frame3, text='tan', width =13, command=lambda:bouton_tan()).grid(row =3, column =2)
divis=Button(Frame3, text='÷', width =13, fg="orange", command=lambda:bouton_click("/")).grid(row =3, column =3)
bou1 = Button(Frame3, text='7', width =13, command=lambda:bouton_click(7),).grid(row =4, column =0)
bou2 = Button(Frame3, text='4', width =13, command=lambda:bouton_click(4)).grid(row =5, column =0)
bou3 = Button(Frame3, text='1', width =13, command=lambda:bouton_click(1)).grid(row =6, column =0)
bou4 = Button(Frame3, text='8', width =13, command=lambda:bouton_click(8)).grid(row =4, column =1)
bou5 = Button(Frame3, text='5', width =13, command=lambda:bouton_click(5)).grid(row =5, column =1)
bou6 = Button(Frame3, text='2', width =13, command=lambda:bouton_click(2)).grid(row =6, column =1)
bou7 = Button(Frame3, text='9', width =13, command=lambda:bouton_click(9)).grid(row =4, column =2)
bou8 = Button(Frame3, text='6', width =13, command=lambda:bouton_click(6)).grid(row =5, column =2)
bou9 = Button(Frame3, text='3', width =13, command=lambda:bouton_click(3)).grid(row =6, column =2)
bou0 = Button(Frame3, text='0', width =13, command=lambda:bouton_click(0)).grid(row =7, column =1)
boupoint = Button(Frame3, text='.', width =13, command=lambda:bouton_click(".")).grid(row =7, column =0)
racine = Button(Frame3, text='√', width =13, activebackground='yellow', command=lambda:bouton_click("**0.5")).grid(row =7, column =2)
bouegale = Button(Frame3, text='EXE', width =13, borderwidth=3, fg="orange", activebackground='yellow', command=lambda:bouton_egal()).grid(row =7, column =3)
bouplus = Button(Frame3, text='+', width =13, fg="orange", command=lambda:bouton_click("+")).grid(row =4, column =3)
boumoins = Button(Frame3, text='-', width =13, fg="orange", command=lambda:bouton_click("-")).grid(row =5, column =3)
boufois = Button(Frame3, text='x', width =13, fg="orange", command=lambda:bouton_click("*")).grid(row =6, column =3)



   

fen.mainloop()
