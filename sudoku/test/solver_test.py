import unittest
from solver import Solver
from square import Square
Solver()

class SudokuPuzzleSolverTest(unittest.TestCase):

    def test_is_valid(self):
        puzzle = [
                    [
                        Square(1,1,1,1),
                        Square(4,1,2,1),
                        Square(3,1,3,2),
                        Square(2,1,4,2)
                    ],
                    [
                        Square(3,2,1,1),
                        Square(2,2,2,1),
                        Square(4,2,3,2),
                        Square(1,2,4,2)
                    ],
                    [
                        Square(4,2,1,3),
                        Square(1,2,2,3),
                        Square(2,2,3,4),
                        Square(3,2,4,4)
                    ],
                    [
                        Square(2,2,1,3),
                        Square(3,2,2,3),
                        Square(1,2,3,4),
                        Square(4,2,4,4)
                    ]
                ]
        solver = Solver()
        self.assertTrue(solver.is_valid(puzzle))

if __name__ == '__main__':
    unittest.main()
