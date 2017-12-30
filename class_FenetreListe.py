from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import class_FenetrePropos
import class_FenetreCree
import class_FenetreMere
import class_ListRegle

class FenetreListe(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        #Creation de la barre de menu
        self.barremenu = tk.Menu(self.master)

        #Creation du menu "Regles"
        self.regles = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "Regles", underline = 0, menu = self.regles)
        self.regles.add_command(label = "Renommage", underline = 0, command = self.renommage)
        self.regles.add_command(label = "Creer une regle", underline = 0, command = self.creer)
        self.regles.add_command(label = "Quitter", underline = 0, command = self.quitter)
        
        #Creation du menu "?"
        self.aide = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "?", underline = 0, menu = self.aide)

        #Afficher le menu
        self.master.config(menu = self.barremenu)
        
        #TOP
        self.lisR = class_ListRegle.ListRegle()
        self.lisR.charger()
            
        top = LabelFrame(self.master, padx=10, pady=0, relief = FLAT )
        top.pack(fill="both", expand=Y, side=TOP)
        self.cb_regle = ttk.Combobox(top, value =  self.lisR)
        self.cb_regle.pack()

        #BOT
        bot = LabelFrame(self.master, padx=10, pady=0, relief = FLAT )
        bot.pack(fill="both", expand=Y, side=BOTTOM)
        Button(bot, text ='Afficher la regle', command= self.afficher).pack(side = BOTTOM, expand=Y)
        Button(bot, text ='Supprimer toutes les regles', command= self.supprimer).pack(side = BOTTOM, expand=Y)
    #Premier onglet du menu
    def creer(self):
        nouvel_fenetre = tk.Tk()
        nouvel_fenetre.title("Creation d'une regle")
        fenetre_creer = class_FenetreCree.FenetreCree(nouvel_fenetre)

    def renommage(self):
        nouvel_fenetre = tk.Tk()
        nouvel_fenetre.title("Renommage")
        fenetre_liste = class_FenetreMere.FenetreMere(nouvel_fenetre)

        
    def quitter(self): self.master.destroy()
    
    def supprimer(self):
        open(self.lisR.fichier, 'w').write("")
        messagebox.showinfo("Done!", "Regles supprimees")
        self.quitter()
        
    def afficher (self):
        messagebox.showinfo(self.cb_regle.get(), self.lisR.regle[self.cb_regle.current()])

    #Deuxieme onglet du menu
    def apropos(self):
        nouvel_fenetre = tk.Tk()
        nouvel_fenetre.title("A propos")
        fenetre_apropos = class_FenetrePropos.FenetrePropos(nouvel_fenetre)

