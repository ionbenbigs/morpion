class Grille:
    def __init__( self , taillex , tailley ):
        self.taillex = taillex
        self.tailley = tailley
        self.grille = []
        self.creer_grille()
        self.affichage_grille()

    
    def creer_grille(self):
        icone = 'X'
        for i in range (self.taillex):
            ligne=[]
            for j in range(self.tailley):                         
                ligne.append(icone)
            self.grille.append(ligne)

    def affichage_grille(self):
        pass


g = Grille(3,3)
print(g.grille)