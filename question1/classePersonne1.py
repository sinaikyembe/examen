class Personne:
    def __init__(self, nom_E, prenom_E, age_E):
        self.nom = nom_E
        self.prenom = prenom_E
        self.age= age_E
        
    def afficherInfo(self):
        print(f"bonjour monsieur {self.nom} {self.prenom} vous avais {self.age} ans")

personne1= Personne("Senga", "Emma", "20")
personne1.afficherInfo()