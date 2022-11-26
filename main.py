#Import tkinter library
from tkinter import *
from tkinter import ttk


def detecteLangue(textValue):
    """
        Détection de la langue
    """
    return 'todo'

def get_value():
    """
        Récupération de du texte et affichage du résultat
    """
    textValue=text.get("1.0",END)
    langueDetection = detecteLangue(textValue)
    detection.delete(1.0, END)
    detection.insert(END, langueDetection)


win= Tk()
win.geometry("500x250")

#Création des widgets de type Text
text = Text(win, height=3, width=55)
detection = Text(win, height=1, width=55)

#Création du bouton
button = ttk.Button(win, text="Détecter", command= get_value)

#Création des widgets de type label
labelText = Label(win, text='Text :', anchor='w')
labelDetection =Label(win, text='Détection :', anchor='w')

#placement des widgets dans la fenetre
labelText.pack(fill='both', padx=20, pady=10)
text.pack()
button.pack(pady=10)
labelDetection.pack(fill='both', padx=20, pady=10)
detection.pack()

win.mainloop()


