"""Cette classe est le système d'affichage du jeu de la vie.
Elle utilise pygame pour afficher le jeu dans une fenêtre.
Elle gère aussi toutes les interactions avec le joueur.
"""

import pygame
import datetime as dt

from game_of_life import const


class GameDisplayer:
    """Classe qui gère l'affichage du jeu.
    """

    def __init__(self, parent, size: tuple[int, int], cell_size: int):
        """Initialise le système d'affichage du jeu.
        """
        self.parent = parent
        self.size: tuple[int, int] = size
        self.cell_size: int = cell_size
        self.running: bool = False
        self.clicked: tuple[int, int] = (-1, -1)

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

    def handle_events(self):
        """Met à jour les infos de statut du jeu.
        """
        for event in pygame.event.get():
            # Fermer normalement
            if event.type == pygame.QUIT:
                self.parent.quit()

            elif event.type == pygame.KEYDOWN:
                # Fermer avec echap
                if event.key == pygame.K_ESCAPE:
                    self.parent.quit()

                # Mettre en pause avec espace
                elif event.key == pygame.K_SPACE:
                    self.parent.toggle_paused()

                # Remettre à zéro avec r
                elif event.key == pygame.K_r:
                    self.parent.reset_grid()

                # Sauvegarder avec s
                elif event.key == pygame.K_s:
                    self.parent.save_grid(
                        "Save " +\
                        dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    )

                # Template à l'endroit avec ↑
                elif event.key == pygame.K_UP:
                    self.parent.rotate_template(0)

                # Template à l'envers avec ↓
                elif event.key == pygame.K_DOWN:
                    self.parent.rotate_template(2)

                # Template à gauche avec ←
                elif event.key == pygame.K_LEFT:
                    self.parent.rotate_template(1)

                # Template à droite avec →
                elif event.key == pygame.K_RIGHT:
                    self.parent.rotate_template(3)
                

                # Charger les templates avec FX
                elif event.key in const.TEMPLATE_KEYS:
                    self.parent.load_template(
                        const.TEMPLATE_KEYS.index(event.key)+1
                    )
            
            # Détection du clic
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.parent.toggle_cell(
                        event.pos[0] // self.cell_size,
                        event.pos[1] // self.cell_size
                    )

            # Détection du scroll
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.parent.raise_speed()
                elif event.y < 0:
                    self.parent.lower_speed()

    def quit(self):
        """Ferme la fenêtre pygame.
        """
        pygame.quit()
