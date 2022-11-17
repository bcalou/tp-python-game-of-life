"""Cette classe est le système d'affichage du jeu de la vie.
Elle utilise pygame pour afficher le jeu dans une fenêtre.
Elle gère aussi toutes les interactions avec le joueur.
"""

import pygame

from game_of_life import const


class GameDisplayer:
    """Classe qui gère l'affichage du jeu.
    """

    def __init__(self, size: tuple[int, int], cell_size: int):
        """Initialise le système d'affichage du jeu.
        """
        self.size = size
        self.cell_size = cell_size
        self.closing = False
        self.running = True

        self.screen = pygame.display.set_mode((
                self.size[0] * self.cell_size,
                self.size[1] * self.cell_size
        ))
        pygame.display.set_caption("Game of Life")

    def draw(self, grid: list[list[int]]):
        """Dessine la grille du jeu.
        """
        self.screen.fill(const.BACKGROUND_COLOR)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    pygame.draw.rect(self.screen, const.CELL_COLOR, (
                        x * self.cell_size, y * self.cell_size,
                        self.cell_size, self.cell_size
                    ))

        pygame.display.flip()

    def update_state(self):
        """Met à jour les infos de statut du jeu.
        """
        for event in pygame.event.get():
            # Fermer normalement
            if event.type == pygame.QUIT:
                self.closing = True

            elif event.type == pygame.KEYDOWN:
                # Fermer avec echap
                if event.key == pygame.K_ESCAPE:
                    self.closing = True
                # Mettre en pause avec espace
                elif event.key == pygame.K_SPACE:
                    self.running = not self.running

    def is_running(self) -> bool:
        """Vérifie si le jeu est en cours.
        """
        self.update_state()
        return self.running

    def is_closing(self) -> bool:
        """Vérifie si la fenêtre est en train de se fermer.
        """
        self.update_state()
        return self.closing

    def quit(self):
        """Ferme la fenêtre pygame.
        """
        pygame.quit()
