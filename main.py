from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import class_FenetrePropos
import class_FenetreListe
import class_FenetreCree
import class_FenetreMere
    
fenetre = tk.Tk()
fenetre.title("Renommage")
app = class_FenetreMere.FenetreMere(fenetre)
fenetre.mainloop()