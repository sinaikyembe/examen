import classePersonne1

class Enseignat(classePersonne1.Personne):
    def __init__(self, nom_E, prenom_E, age_E, matiere_enseigner):
        super().__init__(nom_E, prenom_E, age_E)
        self.matiere= matiere_enseigner
    
    def afficherInfo(self):
        print(f"monsieur {self.nom} {self.prenom} vous avais {self.age} ans, la matiere enseignée {self.matiere}")
 
enseignat1 = Enseignat(" Monsieur tshibaka ", "Daniel", 32, "Base de donnée")
enseignat1.afficherInfo()