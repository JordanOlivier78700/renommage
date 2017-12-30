import class_Action
import class_Regle
import os
import glob
class Renommage (class_Action.Action):
    """
        Renommage hérite de la classe Action
        nom_Repertoire
        regle
    """
    def __init__(self, rpt, rgl):
        class_Action.Action.__init__(self, rpt, rgl)
    def __str__(self):
        return ""
    def get_nom_Repertoire(self):
        return class_Action.Action.get_nom_Repertoire(self)
    def get_regle(self):
        return class_Action.Action.get_regle(self)
    def set_nom_Repertoire(self, rpt):
        class_Action.Action.set_nom_Repertoire(self,rpt)
    def set_regle(self, rgl):
        class_Action.Action.set_regle(self,rgl)
    def fichiers_to_rename(self):
        return class_Action.Action.fichiers_to_rename(self)
    def avant_apres(self, fichier):
        return class_Action.Action.avant_apres(self, fichier)
    def rename(self):
        os.chdir(self.path_rep)
        test = self.fichiers_to_rename()
        save_apt = self.ma_regle.apartirde
        cpt=0
        tmp=""
        for f in test:
            av , ap =self.avant_apres(f)
            if self.ma_regle.amorce == "000":
                if self.ma_regle.apartirde != "":
                    tmp = str(int(self.ma_regle.apartirde)+cpt)
                else:
                    tmp = str(cpt)
            if self.ma_regle.amorce == "AAA" and cpt != 0:
                if  self.ma_regle.apartirde != "" :
                    self.ma_regle.apartirde = self.inc_letter(self.ma_regle.apartirde)
                    tmp = self.ma_regle.apartirde
                else: 
                    self.ma_regle.apartirde = self.inc_letter(self.ma_regle.amorce)
                    tmp = self.ma_regle.apartirde
            if self.ma_regle.amorce == "AAA":
                if self.ma_regle.apartirde != "":
                    tmp=self.ma_regle.apartirde
                else:
                    tmp = "AAA"
            ap = tmp+ap[3:]
            os.rename(av, ap)
            cpt +=1
        self.ma_regle.apartirde = save_apt
        return cpt
            
    def inc_letter(self, lettres):
        """
            Recupe 3 lettre et incremente ==> AAZ + 1 = ABA
            AZZ => BAA
            ZZZ => AAA
            AAZ => ABA
            AZA => AZB
            
        """
        list_lettre= list(lettres)
        if list_lettre[2] == "Z":
            if list_lettre[1] =="Z":
                if list_lettre[0]=="Z":
                    return "AAA"
                else:
                    return chr(ord(list_lettre[0]) + 1)+"AA"
            else: 
                return list_lettre[0]+chr(ord(list_lettre[1]) + 1)+"A"
        else:
            return list_lettre[0]+list_lettre[1]+chr(ord(list_lettre[2]) + 1)
        
"""
path = "C:/Users/L0460978/Desktop/Fait_Marquant/cc"
mr = class_Regle.Regle("ABZ","pre","post",".txt","AAA","coucou")
act = Renommage(path, mr)
act.rename()
"""