"""La Cellule est un modèle (voir principe du MVC).
Elle représente une cellule de la grille de jeu.
"""

class Cellule():
    """Classe représentant une cellule de la grille de jeu.
    Elle contient l'état de la cellule, ainsi que les méthodes pour la manipuler.
    """
    def __init__(self, x: int, y: int, alive: bool):
        """Constructeur de la classe Cellule.
        Il prend en paramètre la position de la cellule et son état.
        """
        self.x: int = x
        self.y: int = y
        self.alive: bool = alive

    def __str__(self) -> str:
        """Méthode qui permet d'afficher une cellule.
        """
        return "Cellule en position (" + str(self.x) + ", " + str(self.y) + ")" + \
            " alive : " + str(self.alive)

    def get_alive(self) -> bool:
        """Méthode qui permet de récupérer l'état d'une cellule.
        """
        return self.alive

    def kill(self) -> None:
        """Méthode qui permet de tuer une cellule.
        """
        self.alive = False

    def revive(self):
        """Méthode qui permet de faire revivre une cellule.
        """
        self.alive = True

    def get_position(self):
        """Méthode qui permet de récupérer la position d'une cellule.
        """
        return (self.x, self.y)
