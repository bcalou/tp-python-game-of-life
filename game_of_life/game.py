TypeState = list[list[int]]


class Game:

    def __init__(self, state: TypeState):
        self._state = state

    def get_state(self) -> TypeState:
        return self._state

    def change_state(self, next_state: TypeState):
        self._state = next_state

    def get_next_state(self):
        # Fonction de passage d'étape
        stock: TypeState = []
        for row in range(0, len(self.get_state())):

            # Ajout d'une nouvelle ligne pour chaque ligne dans l'état de base
            stock.append([])
            for col in range(0, len(self.get_state()[0])):

                # Je créai une variable ou j'ajoute l'état de tout les voisins
                # pour déterminer le prochaine état de la cellule
                total_neighbour: int = 0
                for y in range(-1, 2):

                    for x in range(-1, 2):

                        if ((len(self.get_state()) > (row - y) >= 0) and (len(self.get_state()[0]) > (col - x) >= 0)):

                            total_neighbour += self.get_state()[row-y][col-x]
                total_neighbour -= self.get_state()[row][col]
                # En fonction de l'état d'origine de la cellule et du résultat
                # des voisins, je lui applique sont prochaine état
                if self.get_state()[row][col] == 1:

                    if not 2 <= total_neighbour <= 3:

                        stock[row].append(0)
                    else:

                        stock[row].append(1)
                else:

                    if total_neighbour == 3:

                        stock[row].append(1)
                    else:

                        stock[row].append(0)
        self.change_state(stock)
