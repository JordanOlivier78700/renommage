from tkinter import *
import tkinter as tk

class FenetrePropos(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        Button(fenetre, text ="watch", relief=RAISED, cursor="watch").pack()
        showinfo("Informations gÃ©nÃ©rales", "Programme crÃ©Ã© par Cyril DANIELS dans le cadre de la formation L3 M2i. \n\nVersion 0.1a \n\nOui j'ai galÃ©rÃ© Ã  faire ce Programme. \nBeaucoup.")
