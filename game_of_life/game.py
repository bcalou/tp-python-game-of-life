from game_of_life.types import Coordinates
from game_of_life.board import Board
from game_of_life.state import State


class Game:
    """
    Handles the game of life rules
    See https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for details
    """

    def __init__(self, board: Board, state: State):
        self._board: Board = board
        self._state: State = state

        # This will be used to compute the next state
        self._next_game_state: State

        # The first state needs no computation, let's draw it immediatly
        self._state.for_each_cell_alive(self._board.draw_cell)

        # Commit to the screen
        self._board.commit()

    def update(self):
        """Main loop for the game, compute and draw the next state"""
        # First, erase everything
        self._board.clear()

        self._compute_next_game_state()

        # All cells are ready to be painted, update the board
        self._board.commit()

    def _compute_next_game_state(self):
        """Compute the next state according to the game of life's laws"""
        # Generate an empty matrix that will store the next state
        # We need to do this to keep the initial state intact while we
        # check for changes
        self._next_game_state = self._state.get_new_empty_state()

        # Compute the next game state by looking at each cell of the current
        # game state
        self._state.for_each_cell(self._test_cell_for_next_state)

        # The next state replaces the current state
        self._state = self._next_game_state

    def _test_cell_for_next_state(self, coordinates: Coordinates):
        """Test if the cell should live and add it to the next state"""

        # How many neighbours does this cell have?
        neighbours_count = self._state.get_neighbours_count(coordinates)

        # A living cell survives if it has 2 or 3 neighbours
        cell_survives = (
          self._state.is_alive(coordinates)
          and 2 <= neighbours_count <= 3
        )

        # A dead cell becomes alive if it has 3 neighbours
        cell_births = neighbours_count == 3

        if cell_survives or cell_births:
            # Draw the cell and mark it as alive in the next game state

            self._board.draw_cell(coordinates)
            self._next_game_state.set_cell_state(coordinates, State.ALIVE)
