import classePersonne1

class Etudiant(classePersonne1.Personne):
    def __init__(self, nom_E, prenom_E, age_E,num_E ):
        super().__init__(nom_E, prenom_E, age_E,)
        self.num= num_E
        
    
    def AfficherInfo(self):
        print(f"{self.nom} {self.prenom} tu as {self.age} ans, votre numero {self.num}")
 
Etudiant = Etudiant (" kyembe", "sinai", 22, 997442398)
Etudiant.afficherInfo()