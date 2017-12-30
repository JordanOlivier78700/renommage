import class_Regle
import glob

class Action :
    """
        Action:
        path_rep = String
        C:/Users/xxxx/Documents
        ma_regle = Regle
    """
    def __init__(self, rep, rgl):
        self.path_rep = rep
        self.ma_regle = rgl
	
    def __str__(self):
        return ""
	
    def get_path_rep(self):
        return self.path_rep
	
    def get_ma_regle(self):
        return self.ma_regle

    def set_path_rep(self, rpt):
        self.path_rep = rpt
	
    def set_ma_regle(self, rgl):
        self.ma_regle = rgl
	
    def avant_apres(self, fichier):
        tmp = fichier.split("\\")
        avant2 = tmp[len(tmp)-1]

        apres = ""
        if self.ma_regle.amorce != "" and self.ma_regle.apartirde == "":
            apres += self.ma_regle.amorce+"_"
        elif self.ma_regle.amorce != "" and self.ma_regle.apartirde != "":
            apres += self.ma_regle.apartirde+"_"
        apres += self.ma_regle.prefix
        if self.ma_regle.nomfichier :
            apres += self.ma_regle.nomfichier
            apres += self.ma_regle.postfix
            if self.ma_regle.extension != "":
                apres += self.ma_regle.extension
            else:
                tmp = fichier.split("\\")
                fch = tmp[len(tmp)-1]
                tmp2 = fch.split('.')
                apres += "."+tmp2[len(tmp2)-1]    
        else :
                tmp = fichier.split("\\")
                fch = tmp[len(tmp)-1]
                tmp2 = fch.split(".")
                apres += tmp2[0]
                apres += self.ma_regle.postfix
                if self.ma_regle.extension != "":
                    apres += self.ma_regle.extension
                else:
                    tmp = fichier.split("\\")
                    fch = tmp[len(tmp)-1]
                    tmp2 = fch.split('.')
                    apres += "."+tmp2[len(tmp2)-1] 
        return (avant2, apres)
    def fichiers_to_rename(self):
        """
            Renvoie la liste de fichier du repertoire ayant la bonne extension
        """
        print(self.ma_regle.extension)
        if self.ma_regle.extension != "":
            ma_list = glob.glob(self.path_rep+"/*"+self.ma_regle.extension)
        else:
            ma_list = glob.glob(self.path_rep+"/*.*")
        print(ma_list)
        return ma_list
"""		
path = "C:/Users/L0460978/Desktop/Fait_Marquant/cc"
mr = class_Regle.Regle("","pre","post","","AAA","coucou")
act = Action(path, mr)
print(act.avant_apres())
print(act.fichiers_to_rename())
""" 