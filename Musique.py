
from pydantic import BaseModel, ValidationError,validator

class Musique(BaseModel):
    titre: str
    nom: str
    prenom: str
    immatriculation: str
    type_musique: str
    duration: int

    # def __init__(self, titre, nom, prenom, immatriculation, type, duration):
    #     self.titre = titre
    #     self.nom = nom
    #     self.prenom = prenom
    #     self.immatriculation = immatriculation
    #     self.type_musique = type
    #     self.duration = duration

    @validator('type_musique')
    def check_type_musique(cls, v,values):
        if v not in ["RAP", "POP", "RNB"]:
            raise ValueError("Le type de musique doit être RAP, POP ou RNB")
        return v
    
    @validator('immatriculation')
    def check_immatriculation(cls, v,values):
        if len(v)!= 15:
            raise ValueError("L'immatriculation doit être de 15 chiffres")
        if v[0].upper() != values['nom'][0].upper() or v[1].upper() != values['prenom'][0].upper():
            raise ValueError("Le type de musique doit commencer par la première lettre du nom et du prénom")
        if v[2] != "/"  or v[6] != "/"  or v[10] != "/" :
            raise ValueError("Le type de musique doit être de la forme XX/XXX/XXX/XXXX")
        if int(v[3:6]) < 60 or int(v[3:6]) >300:
            raise ValueError("La duration doit être comprise entre 1 et 5")
        if v[7:10] not in ['RNB', 'RAP', 'POP']:
            raise ValueError("Le type de musique doit être RAP, POP ou RNB")    
        if '6' in v[11:15]:
            raise ValueError("Le dernier bloc ne doit pas contenir le chiffre 6")     
        return v
    
    



    





