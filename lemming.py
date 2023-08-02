class Lemming():
    # Constructeur
    def __init__(self, l, c, d, j):
        self._ligne = l
        self._colonne = c
        self._direction = d
        self._jeu = j

    # Cette méthode renvoie ’>’ ou ’<’ selon la direction du lemming
    def __str__(self):
        if self._direction == 1:
            return ")"
        else:
            return "("

    # Cette fonction déplace ou retourne le lemming
    def action(self):
        # Si la case sous le lemming est vide, il va tomber d'une case en dessous
        if self._jeu[self._ligne+1][self._colonne].libre():
            self._jeu[self._ligne][self._colonne].depart()
            self._jeu[self._ligne+1][self._colonne].arrivee(self)
            self._ligne += 1
        # si la case devant le lemming (selon la direction) est libre il avance
        elif self._jeu[self._ligne][self._colonne+self._direction].libre():
            self._jeu[self._ligne][self._colonne].depart()
            self._jeu[self._ligne][self._colonne+self._direction].arrivee(self)
            self._colonne += self._direction
        # sinon il se retourne
        else:
            self._direction = -self._direction

    # Cette fonction retire le lemming du jeu
    def sort(self):
        self._jeu._saved += 1
        self._jeu._lemmings.remove(self)