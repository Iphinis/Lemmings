# Importation des autres fichiers qui contiennent des classes
import lemming
import case

class Jeu():
    # Constructeur
    def __init__(self, cave, lemmings):
        self._cave = cave

        self._file = open('cave_lemmings.txt', 'r')
        self._content = self._file.read()
        self._file.close()

        self._lines = self._content.split('\n')

        self._pos = self._lines[0].replace('[','').split(']')
        self._start = []
        self._start.append(int(self._pos[0]))
        self._start.append(int(self._pos[1]))

        # on supprime les positions de départ (ligne 0) du tableau des lignes
        self._lines.pop(0)

        # création des cases
        for line in self._lines:
            y = []
            self._cave.append(y)
            for char in line:
                y.append(case.Case(char,None))

        self._lemmings = lemmings
        self._tour = 0

        self._saved = 0

    # Cette fonction affiche la carte avec les positions et directions de tous les lemmings en jeu soit ")" si le lemming regarde à droite et inversement "("
    def affiche(self):
        print("Tour n°" + str(self._tour))
        map = ""
        for y in self._cave:
            for x in y:
                map = map + str(x)
            map = map + "\n"
        print(map)

    # Cette fonction fait agir chaque lemming une fois et affiche le nouvel état du jeu
    def tour(self):
        if len(self._lemmings) > 0:
            self._tour += 1
            for lem in self._lemmings:
                lem.action()
        self.affiche()

    # Cette fonction ajoute un lemming dans le jeu
    def ajouter_lemming(self):
        lem = lemming.Lemming(self._start[0],self._start[1],1,self)
        self._cave[self._start[0]][self._start[1]] = case.Case(" ",lem)
        self._lemmings.append(lem)
        self.affiche()

    # Cette fonction lance une boucle infinie attendant des commandes de l’utilisateur.
    def demarre(self):
        print('Commandes:\n- "l": Ajouter un lemming\n- "q": Quitter\n- "j": Jouer un tour\n- "s": Statistiques\n')
        isRunning = True
        while isRunning:
            cmd = str(input("~\jeu $ "))
            if cmd == "help":
                print('Commandes:\n- "l": Ajouter un lemming\n- "q": Quitter\n- "j": Jouer un tour\n- "s": Statistiques\n')
            elif cmd == "l":
                self.ajouter_lemming()
            elif cmd == "q":
                isRunning = False
            elif cmd == "j":
                self.tour()
            elif cmd == "s":
                print("Tour n°" + str(self._tour) + "\nLemmings en jeu: " + str(len(self._lemmings)) + "\nLemmings sauvés: " + str(self._saved) + "\n")
            else:
                print(cmd + " n'est pas une commande reconnue, veuillez reessayer.\n")

    # Cette méthode spéciale renvoie un élément de _cave
    def __getitem__(self, l):
        return self._cave[l]

# Création de l'instance de la classe Jeu
j = Jeu([], [])
