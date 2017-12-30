from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import class_FenetrePropos
import class_FenetreListe
import class_FenetreMere
import class_Regle
import class_ListRegle

class FenetreCree(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        #Creation de la barre de menu
        self.barremenu = tk.Menu(self.master)

        #Creation du menu "Regles"
        self.regles = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "Regles", underline = 0, menu = self.regles)
        self.regles.add_command(label = "Renommage", underline = 0, command = self.renommage)
        self.regles.add_command(label = "Lister les regles", underline = 0, command = self.lister)
        self.regles.add_command(label = "Quitter", underline = 0, command = self.quitter)

        #Creation du menu "?"
        self.aide = tk.Menu(self.barremenu, tearoff = 0)
        self.barremenu.add_cascade(label = "?", underline = 0, menu = self.aide)

        #Afficher le menu
        self.master.config(menu = self.barremenu)
        
        
        #TOP
        top = LabelFrame(self.master, padx=10, pady=0, relief = FLAT )
        top.pack(fill="both", expand=Y, side=TOP)
        label = Label(top, text="Creer une regle")
        label.pack()      
        
            #RIGHT (photo)
        top_right = LabelFrame(top, padx=10, pady=0, relief = FLAT )
        top_right.pack(fill="both", expand="no", side=RIGHT)
        photo = ImageTk.PhotoImage(file='fond.gif', name='fond', master= top_right )
        canvas = tk.Canvas(top_right, width = 200, height = 150)
        canvas.create_image(100,50,image=photo) 
        canvas.pack()
        
        #BOT
        bot = LabelFrame(self.master, padx=20, pady=20 , relief = FLAT)
        bot.pack(fill="both", expand=Y)

        #BOT left
        bot_left = LabelFrame(bot, padx=0, pady=10, relief = FLAT)
        bot_left.pack(fill="both", expand="no", side=LEFT)
            #left
        bot_left_left = LabelFrame(bot_left, padx=0, pady=0, relief = FLAT)
        bot_left_left.pack(fill="both", expand="no", side=LEFT)
        Label(bot_left_left, text="Amorce :").pack()
        self.v1 = tk.IntVar(bot_left_left)
        liste= [("Aucune", 1),("Lettre", 2),("Chiffre", 3)]
        for text, mode in liste:
            b1 = Radiobutton(bot_left_left, text=text, variable=self.v1, value=mode)
            b1.pack(anchor=W)
                #BOT
        bot_left_left_bot = LabelFrame(bot_left_left, padx=0, pady=0, relief = FLAT)
        bot_left_left_bot.pack(fill="both", expand="no", side=LEFT)
        a_partir = StringVar()
        a_partir.set("")
        self.ent_partir = Entry(bot_left_left_bot, textvariable=a_partir, width=10)
        self.ent_partir.pack(side = RIGHT)
        Label(bot_left_left_bot, text="A partir de :").pack(side = LEFT)
            #RIGHT
        bot_left_right = LabelFrame(bot_left, padx=0, pady=0, relief = FLAT)
        bot_left_right.pack(fill="both", expand="no", side=LEFT)
        pref = StringVar()
        pref.set("")
        Label(bot_left_right, text="Prefix :").pack(side = TOP)
        self.ent_pref = Entry(bot_left_right, textvariable=pref, width=20)
        self.ent_pref.pack()

        #BOT right
        bot_right = LabelFrame(bot, padx=0, pady=10, relief = FLAT)
        bot_right.pack(fill="both", expand="no", side=RIGHT)
            #left
        bot_right_left = LabelFrame(bot_right, padx=0, pady=0, relief = FLAT)
        bot_right_left.pack(fill="both", expand="no", side=LEFT)
                #left
        bot_right_left_left = LabelFrame(bot_right_left, padx=0, pady=0, relief = FLAT)
        bot_right_left_left.pack(fill="both", expand="no", side=LEFT)
        self.nomoriginal = Checkbutton(bot_right_left_left, text="")
        self.nomoriginal.pack()
        self.nomperso = Checkbutton(bot_right_left_left, text="")
        self.nomperso.pack()        
                #right
        bot_right_left_right = LabelFrame(bot_right_left, padx=0, pady=0, relief = FLAT)
        bot_right_left_right.pack(fill="both", expand="no", side=RIGHT)
        Label(bot_right_left_right, text="Nom du fichier original").pack()
        self.nom_autre = StringVar()
        self.nom_autre.set("Nom personnalise")
        self.ent_autre = Entry(bot_right_left_right, textvariable=self.nom_autre, width=20)
        self.ent_autre.pack( pady = 5)
        

            #right
        bot_right_right = LabelFrame(bot_right, padx=0, pady=0, relief = FLAT)
        bot_right_right.pack(fill="both", expand="no", side=RIGHT)
                #left
        bot_right_right_left = LabelFrame(bot_right_right, padx=0, pady=0, relief = FLAT)
        bot_right_right_left.pack(fill="both", expand="no", side=LEFT)
        Label(bot_right_right_left, text="Postfix :").pack()
        post = StringVar()
        post.set("")
        self.ent_post = Entry(bot_right_right_left, textvariable=post, width=20)
        self.ent_post.pack()
                #right
        bot_right_right_right = LabelFrame(bot_right_right, padx=0, pady=0, relief = FLAT)
        bot_right_right_right.pack(fill="both", expand="no", side=RIGHT)
        Label(bot_right_right_right, text="Fichier concerne :").pack(side = TOP)
        self.v2 = tk.IntVar(bot_right_right_right)
        liste2= [("Image (png, gif, jpg, etc.)", 1),("Video (avi, mkv, mpg, etc.)", 2),("Texte (txt, doc, docx, etc.)", 3),("Tout", 4)]
        for text, mode in liste2:
            b2 = Radiobutton(bot_right_right_right, text=text, variable=self.v2, value=mode)
            b2.pack(anchor=W)
        
        
        Button(bot_right_right_right, text ='Creer', command= self.creer).pack(side = BOTTOM)
        
        self.master.mainloop()

    #Premier onglet du menu
    def lister(self):
        nouvel_fenetre = tk.Tk()
        nouvel_fenetre.title("Lister les regles")
        try:
            fenetre_liste = class_FenetreListe.FenetreListe(nouvel_fenetre)
        except:
            messagebox.showerror("Erreur", "Il n existe aucune regle")
            

    def renommage(self):
        nouvel_fenetre = tk.Tk()
        nouvel_fenetre.title("Renommage")
        fenetre_liste = class_FenetreMere.FenetreMere(nouvel_fenetre)

        
    def quitter(self): self.master.destroy()

    #Deuxieme onglet du menu
    def apropos(self):
        nouvel_fenetre = tk.Tk()
        nouvel_fenetre.title("A propos")
        fenetre_apropos = class_FenetrePropos.FenetrePropos(nouvel_fenetre)
        
        
    #fonction du bouton Creer
    def creer (self):
        """
            Creer un objet de la classe règle
            l'ajoute à la liste présente dans NOMLOGICIEL.ini
        """
        #Recup amorce
        if self.v1.get() == 0:
            messagebox.showerror("Erreur", "Vous n'avez pas selectioner l'amorce")
        elif self.v1.get() == 1:
            amorce = ""
        elif self.v1.get() == 2:
            amorce = "AAA"
        else:
            amorce = "000"
        #Recup a partir de   
        if self.ent_partir.get() == None:
            apartir = ""
        else:
            apartir = self.ent_partir.get()
        #Recup prefix    
        if self.ent_pref.get() == None:
            prefix = ""
        else:
            prefix = self.ent_pref.get()
        #Recup nomfichier   
        if self.ent_autre.get() == None:
            nomfichier = False
        else:
            nomfichier = self.ent_autre.get()
        #Recup postfix    
        if self.ent_post.get() == None:
            postfix = ""
        else:
            postfix = self.ent_post.get()
        #Recup extension
        if self.v2.get() == 0:
            messagebox.showerror("Erreur", "Vous n'avez pas selectioner l'extension")
        elif self.v2.get() == 1:
            extension = ".png"
        elif self.v2.get() == 2:
            extension = ".avi"
        elif self.v2.get() == 3:
            extension = ".txt"
        else :
            extension = ""

        ma_regle = class_Regle.Regle(apartir, prefix, postfix, extension, amorce, nomfichier)
        liste_regle = class_ListRegle.ListRegle([ma_regle])
        liste_regle.sauvegarder()
        self.quitter()

