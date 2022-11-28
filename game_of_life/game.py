

def get_next_state(state_matrix):

    #Filled matrix with 0
    result_matrix = [[0]*len(state_matrix) for i in range(len(state_matrix[0]))] 

    for index_y in range(len(state_matrix)):
        for index_x in range(len(state_matrix[index_y])):
            number_neighbor: int = 0
        
            '''Filter'''
            #Case en haut à gauche
            if index_y > 0 and index_x > 0:
                if state_matrix[index_y - 1][index_x - 1] == 1:
                    number_neighbor += 1
            #Cause en haut
            if index_y > 0:
                if state_matrix[index_y - 1][index_x] == 1:
                    number_neighbor += 1
            #Case en haut à droite
            if index_y > 0 and index_x < len(state_matrix[index_y]) - 1:
                if state_matrix[index_y - 1][index_x + 1] == 1:
                    number_neighbor += 1

            #Case à gauche
            if index_x > 0:
                if state_matrix[index_y][index_x - 1] == 1:
                    number_neighbor += 1                
            #Case à droite
            if index_x < len(state_matrix[index_y]) - 1:
                if state_matrix[index_y][index_x + 1] == 1:
                    number_neighbor += 1
            

            #Case en bas à gauche
            if index_y < len(state_matrix) - 1 and index_x > 0:
                if state_matrix[index_y + 1][index_x - 1] == 1:
                    number_neighbor += 1
            #Case en bas
            if index_y < len(state_matrix) - 1:
                if state_matrix[index_y + 1][index_x] == 1:
                    number_neighbor += 1   
            #Case en bas à droite
            if index_y < len(state_matrix) - 1 and index_x < len(state_matrix[index_y]) - 1:
                if state_matrix[index_y + 1][index_x + 1] == 1:
                    number_neighbor += 1
                    
            
            #une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît)
            if number_neighbor == 3:
                #Cell alive
                result_matrix[index_y][index_x] = 1

            #une cellule vivante possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt.
            elif number_neighbor == 2:
                result_matrix[index_y][index_x] = state_matrix[index_y][index_x]

            elif number_neighbor < 2 or number_neighbor > 3:
                #Cell death
                result_matrix[index_y][index_x] = 0
            

    return result_matrix
