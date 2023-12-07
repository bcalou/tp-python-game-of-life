from game_of_life.game_of_life import GameOfLife, ALIVE, DEAD


class HighLife(GameOfLife):
    """
    Redefines the rule of the original game of life

    Original: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

    Highlife: https://en.wikipedia.org/wiki/Highlife_(cellular_automaton)
    """

    def game_rules(self, cell_state: int, neighbour_count: int) -> int:
        """
        Highlife overwrites the default rule of the game of life.

        Returns the cell state for the next iteration

        The rules are B36/S23

        A cell is born if it has 3 or 6 neighbours

        A cell survives if it has 2 or 3 neighbours

        """
        # A cell stays/becomes alive if it has 3 neighbours
        if cell_state == DEAD and (
           neighbour_count == 3 or neighbour_count == 6):
            return ALIVE
        # A cell stays alive/dead if it has 2 neighbours
        elif neighbour_count == 2 or neighbour_count == 3:
            return cell_state
        # Otherwise the cell dies
        return DEAD
