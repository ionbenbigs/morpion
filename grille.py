class Grille:
    def __init__( self , taillex , tailley ):
        self.taillex = taillex
        self.tailley = tailley
        self.grille = []
        self.creer_grille()
<<<<<<< HEAD
        self.afficher_grille()
=======
        self.affichage_grille()
>>>>>>> a89406d0bd83b071e13769f74bae2d40c650e67d

    
    def creer_grille(self):
        icone = 'X'
        for i in range(self.taillex):
            ligne=[]
            for j in range(self.tailley):                         
                ligne.append(icone)
            self.grille.append(ligne)
    

<<<<<<< HEAD
    def afficher_grille(self):
        icone = 1
        
        for p in range(self.taillex):
            
            for h in range(self.tailley):
                print(f"[{icone}]",end= "")
                icone+=1
            print('')    
=======
    def affichage_grille(self):
        pass


>>>>>>> a89406d0bd83b071e13769f74bae2d40c650e67d
g = Grille(3,3)

# [X] [X] [X]
# [X] [X] [X]
# [X] [X] [X]