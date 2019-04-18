import time;

sectors = [[0,3,0,3], [3,6,0,3], [6,9,0,3],
           [0,3,3,6], [3,6,3,6], [6,9,3,6],
           [0,3,6,9], [3,6,6,9], [6,9,6,9]]
class Sudoku:

    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a list of list of int.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """
        # make a copy of the original grid, so we dont mutate the original
        grid_copy = list(grid)

        if Sudoku.solveSudoko(grid_copy):
            return grid_copy
        else:
            return None

    @staticmethod
    def find_next_empty(grid):
        '''(list of list of int) -> (int, int)
        Find and return the index of the next empty square in grid.
        Return -1, -1 if the grid is full.
        REQ: grid is 9x9
        '''
        # -1, -1 if no empty square
        for i in range(0, 9):
            for j in range(0, 9):
                # 0 means empty 
                if grid[i][j] == 0:
                    return i, j
        return -1, -1
    
    @staticmethod
    def is_valid(grid, i, j, value):
        '''(list of list of int, int, int) -> (bool)
        Check if putting value in cell[i][j] is a valid sudoko move,
        return true if it is valid, otherwise return false.
        Suduko rules: Each number can only appear once in a row, column or box.
        '''
        # check value can only appear once in ith row
        for col in range(0, 9):
            # if theres already value in this ith row then its not ok
            if value == grid[i][col]:
                return False
        # check value can only appear once in jth col
        for row in range(0, 9):
            # if theres already value in this ith row then its not ok
            if value == grid[row][j]:
                return False
        # check the 3x3 box 
        box_row_index = 3 * (i // 3)
        bow_col_index = 3 * (j // 3)
        for r in range(box_row_index, box_row_index + 3):
            for c in range(bow_col_index, bow_col_index + 3):
                if grid[r][c] == value:
                    return False        
        # return True if value in cell[i][j] passed all the check
        return True

    @staticmethod
    def makeImplications(grid, i, j, value):
        '''(list of (list of int), int, int, int) -> list of (int, int, int)
        '''
        global sectors
        grid[i][j] = value
        impl = [(i, j, value)]
        for cur_sect in range(len(sectors)):
            sectInfo = []
            # find missing element in cur_sect sectors
            validSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            for x in range(sectors[cur_sect][0], sectors[cur_sect][1]):
                for y in range(sectors[cur_sect][2], sectors[cur_sect][3]):
                    if grid[x][y] != 0:
                        validSet.remove(grid[x][y])
            # attach copy of validSet to each missing square in sect sector
            for x in range(sectors[cur_sect][0], sectors[cur_sect][1]):
                for y in range(sectors[cur_sect][2], sectors[cur_sect][3]):
                    if grid[x][y] != 0:
                        sectInfo.append([x, y, validSet.copy()])
            for m in range(len(sectInfo)):
                curSectInfo = sectInfo[m]
                # find the set of elements on the row corresponding to m 
                # and remove them
                rowv = set()
                for y in range(0, 9):
                    rowv.add(grid[curSectInfo[0]][y])
                valLeft  = curSectInfo[2].difference(rowv)
                # find the set of elements on the column and remove them
                colv = set()
                for x in range(0, 9):
                    colv.add(grid[x][curSectInfo[1]])
                valLeft = valLeft.difference(colv)
                # check if theres only one value left in vset
                if len(valLeft) == 1:
                    value = valLeft.pop()
                    if Sudoku.is_valid(grid, curSectInfo[0], curSectInfo[1],
                                       value):
                        grid[curSectInfo[0]][curSectInfo[1]] = value
                        impl.append((curSectInfo[0], curSectInfo[1], value))
        return impl

    def undoImplications(grid, impl):
        '''(list of (list of int), list of (int, int, int)) -> None
        '''
        for i in range(len(impl)):
            grid[impl[i][0]][impl[i][1]] = 0
    
            
            
        
    @staticmethod
    def solveSudoko(grid):
        '''(list of list of int)
        Visit empty square row by row, try to fill in 1-9,
        back track when none of the 9 digits is valid
        '''
        next_i, next_j = Sudoku.find_next_empty(grid)
        # if the grid we are solving is full then assume its solved
        if (next_i, next_j) == (-1, -1):
            return True
        # try to solve next empty cell with values 1-9
        for cur_value in range(1, 10):
            # check if putting cur_value in grid[next_i, next_j] is valid
            if Sudoku.is_valid(grid, next_i, next_j, cur_value):
                impl = Sudoku.makeImplications(grid, next_i, next_j, cur_value)
                # try solve the rest of sudoko grid
                if Sudoku.solveSudoko(grid):
                    return True
                # if current grid configuration leads to unsolvable
                Sudoku.undoImplications(grid, impl)
        # if the none of the 1-9 solved the next empty cell
        # this sudoko is unsolvable
        return False



    
    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format. Feel free
        to change this if you need to, it will NOT be 
        used in marking. It is just to help you debug.

        Use as:     Sudoku.printGrid(grid)
        """
        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-"*25)

if __name__ == '__main__':
    easy = [[5,1,7,6,0,0,0,3,4],
            [2,8,9,0,0,4,0,0,0],
            [3,4,6,2,0,5,0,9,0],
            [6,0,2,0,0,0,0,1,0],
            [0,3,8,0,0,6,0,4,7],
            [0,0,0,0,0,0,0,0,0],
            [0,9,0,0,0,0,0,7,8],
            [7,0,3,4,0,0,5,6,0],
            [0,0,0,0,0,0,0,0,0]]
    Sudoku.printGrid(easy)
    easy_result = Sudoku.solve(easy)
    Sudoku.printGrid(easy_result)
    '''
    hard = [[0,0,5,3,0,0,0,0,0],
            [8,0,0,0,0,0,0,2,0],
            [0,7,0,0,1,0,5,0,0],
            [4,0,0,0,0,5,3,0,0],
            [0,1,0,0,7,0,0,0,6],
            [0,0,3,2,0,0,0,8,0],
            [0,6,0,5,0,0,0,0,9],
            [0,0,4,0,0,0,0,3,0],
            [0,0,0,0,0,9,7,0,0]]
    Sudoku.printGrid(hard)
    hard_result = Sudoku.solve(hard)
    Sudoku.printGrid(hard_result)'''