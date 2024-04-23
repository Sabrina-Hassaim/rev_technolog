from pydantic import BaseModel, Field
from Musique import Musique
from typing import List
import unittest
from unittest.mock import Mock

class Magasin(BaseModel):
    type_magasin: str
    dvd_musique: List[Musique] = Field(default_factory=list)
    vynille_musique: List[Musique] = Field(default_factory=list)


    """    def __init__(self, type_magasin: str):
        super().__init__()  
        self.type_magasin = type_magasin
        self.dvd_musique = [] 
        self.vynille_musique = []"""
    
    def ajouter_dvd_musique(self, musique: Musique):
        if self.type_magasin == musique.type_musique:
            self.dvd_musique.append(musique)

    def ajouter_vynille_musique(self, musique: Musique):
        if self.type_magasin == musique.type_musique:
            self.vynille_musique.append(musique)

    def supprimer_dvd_musique(self, musique: Musique):
        self.dvd_musique.remove(musique)
    
    def supprimer_vynille_musique(self, musique: Musique):
        self.vynille_musique.remove(musique)
    

class TestMagasin(unittest.TestCase):
    def setUp(self):
        self.magasin = Magasin(type_magasin="POP")
        self.musique = Mock(titre="Titre", nom="Nom", prenom="Prenom", immatriculation="NP/090/POP/1234", type_musique="POP", duration=90)

    def test_ajouter_dvd_musique(self):
        self.magasin.ajouter_dvd_musique(self.musique)
        self.assertIn(self.musique, self.magasin.dvd_musique)

    def test_ajouter_vynille_musique(self):
        self.magasin.ajouter_vynille_musique(self.musique)
        self.assertIn(self.musique, self.magasin.vynille_musique)

if __name__ == '__main__':
    unittest.main()