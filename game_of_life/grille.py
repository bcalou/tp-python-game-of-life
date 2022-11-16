"""La Grille est un modèle (voir principe du MVC).
Elle représente la grille de jeu.

Warnings :
    Pylint a décidé que [] était une valeur par défaut dangereuse. Je préfère ignorer ce warning.
"""
from game_of_life.cellule import Cellule


class Grille:
    """Classe représentant la grille de jeu.
        Elle contient la liste des cellules, ainsi que les méthodes pour les manipuler.
    """
    def __init__(self, largeur: int, hauteur: int, cellules_vivantes: list[tuple[int, int]] = []):
        """Constructeur de la classe Grille.
        Il prend en paramètre la largeur et la hauteur de la grille, ainsi que la liste des cellules vivantes.
        """
        # Stockage des arguments
        self.largeur: int = largeur
        self.hauteur: int = hauteur
        self.cellules: list[list[Cellule]] = []

        # Création des cellules
        for y in range(self.largeur):
            self.cellules.append([])
            for x in range(self.hauteur):
                self.cellules[y].append(Cellule(x, y, False))

        # Cellules vivantes
        for cellule in cellules_vivantes:
            self.cellules[cellule[1]][cellule[0]].revive()

    def __str__(self) -> str:
        """Méthode qui permet d'afficher la grille de jeu.
        """
        grille = ""
        for y in range(self.largeur):
            for x in range(self.hauteur):
                if self.cellules[y][x].get_alive():
                    grille += "■"
                else:
                    grille += "□"
            grille += "\n"
        return grille

    def get_cellule(self, x, y) -> Cellule:
        """Méthode qui permet de récupérer une cellule de la grille.
        Elle prend en paramètre la position de la cellule.
        """
        return self.cellules[x][y]

    def get_voisins(self, x, y) -> list[Cellule]:
        """Méthode qui permet de récupérer les voisins d'une cellule.
        Elle prend en paramètre la position de la cellule.
        """
        voisins = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < self.largeur and j >= 0 and j < self.hauteur and not (i == x and j == y):
                    voisins.append(self.cellules[i][j])
        return voisins