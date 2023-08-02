# Importation de lemming.py qui contient la classe Lemming()
import lemming

class Case():
    # Constructeur
    def __init__(self, terrain, lemming):
        self._terrain = terrain
        self._lemming = lemming

    # Cette méthode renvoie le caractère à afficher pour représenter cette case ou son éventuel occupant
    def __str__(self):
        if self._lemming is not None:
            return str(self._lemming)
        return self._terrain

    # Cette fonction renvoie True si la case peut recevoir un lemming (elle n’est ni occupée, ni un mur)
    def libre(self):
        if (self._terrain == " " and self._lemming is None) or self._terrain == '0':
            return True
        return False

    # Cette fonction retire le lemming présent
    def depart(self):
        self._lemming = None

    # Cette fonction place le lemming lem sur la case, ou le fait sortir du jeu si la case était une sortie
    def arrivee(self,lem):
        if self._terrain == '0':
            self._lemming = None
            lem.sort()
            print("Un lemming a trouve la sortie !")
        elif self.libre():
            self._lemming = lem