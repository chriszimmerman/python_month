import unittest
from solver import Solver
Solver()

class SudokuPuzzleSolverTest(unittest.TestCase):

    def test_is_valid(self):
        puzzle = [[1,4,3,2], [3,2,4,1], [4,1,2,3], [2,3,1,4]]
        solver = Solver()
        self.assertTrue(solver.is_valid(puzzle))

if __name__ == '__main__':
    unittest.main()
