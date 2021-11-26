white = (255, 255, 255)
black = (0, 0, 0)

class Cell:

    def __init__(self, rect : tuple[int, int, int, int], isAlive = False):
        self.isAlive = isAlive
        self.rect = rect
        self.updateColor()

    def updateColor(self):
        if self.isAlive:
            self.color : tuple[int, int, int] = black
        else:
            self.color : tuple[int, int, int] = white

    def setState(self, isAlive):
        self.isAlive = isAlive
        self.updateColor()

    def testSurvivability(self, alive_neighbor):
        if self.isAlive and alive_neighbor in [2, 3]:
            self.setState(True)
        elif not self.isAlive and alive_neighbor == 3:
            self.setState(True)
        else:
            self.setState(False)

    def __repr__(self) -> str:
        return "O" if self.isAlive else "X"