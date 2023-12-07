# class Cell:
    
#     state: bool
#     pos_x: int
#     pos_y: int
    
#     def __init__(self, state: bool, pos_x: int, pos_y: int) -> None:
#         self.state = state
#         self.pos_x = pos_x
#         self.pos_y = pos_y
    
#     def get_state(self) -> bool:
#         return self.state
    
#     def get_pos_x(self) -> int:
#         return self.pos_x
    
#     def get_pos_y(self) -> int:
#         return self.pos_y   
    
#     def get_color(self) -> int:
#         if self.state == True: return 255
#         else: return 0
    
#     def cells_arround(self) -> int:
#         return 0