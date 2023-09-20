from jeton import Jeton
class Grille:
    def __init__( self , taillex , tailley ):
        self.taillex = taillex
        self.tailley = tailley
        self.grille = []
        self.creer_grille()
        self.afficher_grille()

    
    def creer_grille(self):
        jeton=Jeton()
        for i in range(self.taillex):
            ligne=[]
            for j in range(self.tailley):                         
                ligne.append(jeton)
            self.grille.append(ligne)
        

    def afficher_grille(self):
        
        for p in range(self.taillex):
            
            for h in range(self.tailley):
                
                print(f"[{self.grille[p][h].icone}]",end= "")

            print('')    

g = Grille(3,3)

# [[][][]]
