import unittest
from Sudoku import *

class TestSudoku(unittest.TestCase):
    
    def test_easy(self):

        grid = [[5,1,7,6,0,0,0,3,4],
                [2,8,9,0,0,4,0,0,0],
                [3,4,6,2,0,5,0,9,0],
                [6,0,2,0,0,0,0,1,0],
                [0,3,8,0,0,6,0,4,7],
                [0,0,0,0,0,0,0,0,0],
                [0,9,0,0,0,0,0,7,8],
                [7,0,3,4,0,0,5,6,0],
                [0,0,0,0,0,0,0,0,0]]

        soln = [[5,1,7,6,9,8,2,3,4],
                [2,8,9,1,3,4,7,5,6],
                [3,4,6,2,7,5,8,9,1],
                [6,7,2,8,4,9,3,1,5],
                [1,3,8,5,2,6,9,4,7],
                [9,5,4,7,1,3,6,8,2],
                [4,9,5,3,6,2,1,7,8],
                [7,2,3,4,8,1,5,6,9],
                [8,6,1,9,5,7,4,2,3]]
        self.assertEqual(Sudoku.solve(grid), soln)

    def test_diff(self):
        '''
        '''
        grid = [[0,0,5,3,0,0,0,0,0],
                [8,0,0,0,0,0,0,2,0],
                [0,7,0,0,1,0,5,0,0],
                [4,0,0,0,0,5,3,0,0],
                [0,1,0,0,7,0,0,0,6],
                [0,0,3,2,0,0,0,8,0],
                [0,6,0,5,0,0,0,0,9],
                [0,0,4,0,0,0,0,3,0],
                [0,0,0,0,0,9,7,0,0]]

        soln = [[1,4,5,3,2,7,6,9,8],
                [8,3,9,6,5,4,1,2,7],
                [6,7,2,9,1,8,5,4,3],
                [4,9,6,1,8,5,3,7,2],
                [2,1,8,4,7,3,9,5,6],
                [7,5,3,2,9,6,4,8,1],
                [3,6,7,5,4,2,8,1,9],
                [9,8,4,7,6,1,2,3,5],
                [5,2,1,8,3,9,7,6,4]]

        self.assertEqual(Sudoku.solve(grid), soln)

if __name__ == "__main__":
    unittest.main()
