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
                        Square(4,3,1,3),
                        Square(1,3,2,3),
                        Square(2,3,3,4),
                        Square(3,3,4,4)
                    ],
                    [
                        Square(2,4,1,3),
                        Square(3,4,2,3),
                        Square(1,4,3,4),
                        Square(4,4,4,4)
                    ]
                ]
        solver = Solver()
        self.assertTrue(solver.is_valid(puzzle))

    def test_is_valid_return_false_when_two_of_same_number_in_row(self):
        puzzle = [
                    [
                        Square(1,1,1,1),
                        Square(1,1,2,1),
                        Square(1,1,3,2),
                        Square(1,1,4,2)
                    ],
                    [
                        Square(2,2,1,1),
                        Square(2,2,2,1),
                        Square(2,2,3,2),
                        Square(2,2,4,2)
                    ],
                    [
                        Square(3,3,1,3),
                        Square(3,3,2,3),
                        Square(3,3,3,4),
                        Square(3,3,4,4)
                    ],
                    [
                        Square(4,4,1,3),
                        Square(4,4,2,3),
                        Square(4,4,3,4),
                        Square(4,4,4,4)
                    ]
                ]
        solver = Solver()
        self.assertFalse(solver.is_valid(puzzle))
        
    def test_is_valid_return_false_when_two_of_same_number_in_column(self):
        puzzle = [
                    [
                        Square(1,1,1,1),
                        Square(2,1,2,1),
                        Square(3,1,3,2),
                        Square(4,1,4,2)
                    ],
                    [
                        Square(1,2,1,1),
                        Square(2,2,2,1),
                        Square(3,2,3,2),
                        Square(4,2,4,2)
                    ],
                    [
                        Square(1,3,1,3),
                        Square(2,3,2,3),
                        Square(3,3,3,4),
                        Square(4,3,4,4)
                    ],
                    [
                        Square(1,4,1,3),
                        Square(2,4,2,3),
                        Square(3,4,3,4),
                        Square(4,4,4,4)
                    ]
                ]
        solver = Solver()
        self.assertFalse(solver.is_valid(puzzle))

    def test_is_valid_return_false_when_two_of_same_number_in_block(self):
        puzzle = [
                    [
                        Square(1,1,1,1),
                        Square(None,1,2,1),
                        Square(None,1,3,2),
                        Square(None,1,4,2)
                    ],
                    [
                        Square(None,2,1,1),
                        Square(1,2,2,1),
                        Square(None,2,3,2),
                        Square(None,2,4,2)
                    ],
                    [
                        Square(None,3,1,3),
                        Square(None,3,2,3),
                        Square(None,3,3,4),
                        Square(None,3,4,4)
                    ],
                    [
                        Square(None,4,1,3),
                        Square(None,4,2,3),
                        Square(None,4,3,4),
                        Square(None,4,4,4)
                    ]
                ]
        solver = Solver()
        self.assertFalse(solver.is_valid(puzzle))

if __name__ == '__main__':
    unittest.main()
