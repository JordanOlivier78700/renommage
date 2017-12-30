import json
import class_Regle

class ListRegle :
    """
        Regle : une liste !
    """
    def __init__ (self, rgl = [], fch="NOMLOGICIEL.ini"):
        self.regle = rgl
        self.fichier = fch
        	
    def __str__(self):
        ch = ""
        for i in self.regle:
            ch += str(i.nomfichier)+" "
        return ch
    		
    def get_regles (self):
        return self.regle
    	
    def set_regles (self, rgl):
        self.regle =  rgl
        
        
    def deseria(self, obj_dict):
        if obj_dict["__class__"] == "Regle":
            obj = class_Regle.Regle(obj_dict["apartirde"], obj_dict["prefix"],obj_dict["postfix"],obj_dict["extension"],obj_dict["amorce"],obj_dict["nomfichier"] )
            self.regle.append(obj)


    def seria(self, obj):
        if isinstance(obj, class_Regle.Regle):
            return {"__class__": "Regle",
                    "apartirde": obj.apartirde,
                    "prefix": obj.prefix,
                    "postfix": obj.postfix,
                    "extension": obj.extension,
                    "amorce": obj.amorce,
                    "nomfichier": obj.nomfichier}
        raise TypeError(repr(obj) + " n'est pas sérialisable !")
        
    def charger(self):
        """
        Charge un fichier en remplacant
        toute les valeurs de l'objet 
        par les valeurs dans la classe
        """
        with open(self.fichier, 'r', encoding="utf-8") as mon_fichier:
            data =json.load(mon_fichier, object_hook=self.deseria)
            
    def sauvegarder(self):
        if open(self.fichier, 'r').read() != "":
            with open(self.fichier, 'r', encoding="utf-8") as mon_fichier:
                data =json.load(mon_fichier, object_hook=self.deseria)
        with open(self.fichier,'w', encoding='utf-8') as mon_fichier:
                json.dump(self.regle, mon_fichier, indent=4, default=self.seria)
                
                
