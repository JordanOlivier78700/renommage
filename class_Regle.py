

class Regle :
    """
    		
    		apartirde :  String
    		prefix : String
    		postfixe : String
    		extension : .avi, .png, .txt, ""(all)
          amorce : String 000 ==> 999 // A ==> ZZ // ""
      		nomfichier :
					 False = on conserve le nom actuel
					 String = Nouveau nom                     
                     coucou.txt ==> 001_preNOUVEAUNOMpost.txt
                    
    """
    def __init__ (self, aptd, pref, post, ext, amr="", nom=False):
        """
        	Constructeur:
        	Variable par défaut :
        		amr = ""
        		nom = True
        """

        self.apartirde = aptd
        self.prefix = pref
        self.postfix = post
        self.extension = ext
        self.amorce = amr        
        self.nomfichier = nom
        
    def __str__(self):
        chaine="A partir de: "+self.apartirde+" Prefix : "+self.prefix+" Postfix : "+self.postfix+" Extension: "+self.extension+" Amorce: "+self.amorce
        if self.nomfichier :
            chaine += " Nomfichier : "+self.nomfichier
        else :
            chaine += " Nomfichier : "+"<fichier courant>"
        return chaine
		
    def get_amorce(self):
        return self.amorce
	
    def get_apartirde(self):
        return self.apartirde
	
    def get_prefix(self):
        return self.prefix
	
    def get_nomfichier(self):
        return self.nomfichier
	
    def get_postfix(self):
        return self.postfixe

    def set_amorce(self, amrc):
        self.amorce = amrc
	
    def set_apartirde(self, aptd):
        self.apartirde = aptd

    def set_prefix(self, pref):
        self.prefix = pref
	
    def set_nomfichier(self, nom):
        self.nomfichier = nom
	
    def set_postfix(self, post):
        self.postfixe = post