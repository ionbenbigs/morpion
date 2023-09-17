class Grille:
    def __init__( self , taillex , tailley ):
        self.taillex = taillex
        self.tailley = tailley
        self.grille = []
        self.creer_grille()
        self.afficher_grille()

    
    def creer_grille(self):
        icone = 'X'
        for i in range(self.taillex):
            ligne=[]
            for j in range(self.tailley):                         
                ligne.append(icone)
            self.grille.append(ligne)

    def afficher_grille(self):
        icone = 1
        
        for p in range(self.taillex):
            
            for h in range(self.tailley):
                print(f"[{icone}]",end= "")
                icone+=1
            print('')    

g = Grille(3,3)

