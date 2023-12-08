import game_of_life.const as Const

COLOR: int = 255
BORDER_COUNT: int = 4


class Display:

    def draw_cell(self, color: int, position_x: int, position_y: int,
                  size_x: int, size_y: int) -> None:
        """We draw a rect  with color, place and size of rect"""

        Const.pygame.draw.rect(Const.screen, (color, color, color),
                               (position_x, position_y, size_x, size_y))

    def draw_on_screen(self, state: list[list[int]]) -> None:
        """We draw screen cell by cell"""

        # We draw every cell in state with two loop
        for tab_index, tab in enumerate(state):
            for element_index, element in enumerate(tab):

                # We draw cell color
                self.draw_cell(element * COLOR,
                               element_index * Const.MINIMUM_CELL_LENGTH + 1,
                               tab_index * Const.MINIMUM_CELL_LENGTH + 1,
                               Const.MINIMUM_CELL_LENGTH - 2,
                               Const.MINIMUM_CELL_LENGTH - 2)

                # We  draw all border of cell and
                # we define for all border each parameter
                color = ((element+1) % 2) * COLOR
                position_x = element_index * Const.MINIMUM_CELL_LENGTH
                position_y = tab_index * Const.MINIMUM_CELL_LENGTH
                for increment in range(BORDER_COUNT):
                    size_x = Const.MINIMUM_CELL_LENGTH if increment % 2 == 0 \
                        else 1
                    size_y = Const.MINIMUM_CELL_LENGTH if increment % 2 == 1 \
                        else 1
                    if (increment == 2):
                        position_y = (tab_index + 1) \
                            * Const.MINIMUM_CELL_LENGTH - 1
                    if (increment == 3):
                        position_x = (element_index + 1) \
                            * Const.MINIMUM_CELL_LENGTH - 1
                    self.draw_cell(color, position_x, position_y,
                                   size_x, size_y)
