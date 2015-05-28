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

    def test_is_complete(self):
        puzzle = [
                    [
                        Square(1,1,1,1),
                        Square(4,1,2,1),
                        Square(2,1,3,2),
                        Square(3,1,4,2)
                    ],
                    [
                        Square(2,2,1,1),
                        Square(3,2,2,1),
                        Square(4,2,3,2),
                        Square(1,2,4,2)
                    ],
                    [
                        Square(4,3,1,3),
                        Square(1,3,2,3),
                        Square(3,3,3,4),
                        Square(2,3,4,4)
                    ],
                    [
                        Square(3,4,1,3),
                        Square(2,4,2,3),
                        Square(1,4,3,4),
                        Square(4,4,4,4)
                    ]
                ]

        solver = Solver()
        self.assertTrue(solver.is_complete(puzzle))

    def test_is_complete_returns_false_with_blanks(self):
        puzzle = [
                    [
                        Square(None,1,1,1),
                        Square(4,1,2,1),
                        Square(2,1,3,2),
                        Square(3,1,4,2)
                    ],
                    [
                        Square(2,2,1,1),
                        Square(None,2,2,1),
                        Square(None,2,3,2),
                        Square(1,2,4,2)
                    ],
                    [
                        Square(None,3,1,3),
                        Square(None,3,2,3),
                        Square(None,3,3,4),
                        Square(None,3,4,4)
                    ],
                    [
                        Square(3,4,1,3),
                        Square(2,4,2,3),
                        Square(None,4,3,4),
                        Square(None,4,4,4)
                    ]
                ]

        solver = Solver()
        self.assertFalse(solver.is_complete(puzzle))

    def test_solve(self):
        puzzle = [
                    [
                        Square(1,1,1,1),
                        Square(None,1,2,1),
                        Square(2,1,3,2),
                        Square(None,1,4,2)
                    ],
                    [
                        Square(None,2,1,1),
                        Square(None,2,2,1),
                        Square(4,2,3,2),
                        Square(None,2,4,2)
                    ],
                    [
                        Square(None,3,1,3),
                        Square(1,3,2,3),
                        Square(3,3,3,4),
                        Square(None,3,4,4)
                    ],
                    [
                        Square(3,4,1,3),
                        Square(None,4,2,3),
                        Square(None,4,3,4),
                        Square(4,4,4,4)
                    ]
                ]

        expected = [
                    [
                        Square(1,1,1,1),
                        Square(4,1,2,1),
                        Square(2,1,3,2),
                        Square(3,1,4,2)
                    ],
                    [
                        Square(2,2,1,1),
                        Square(3,2,2,1),
                        Square(4,2,3,2),
                        Square(1,2,4,2)
                    ],
                    [
                        Square(4,3,1,3),
                        Square(1,3,2,3),
                        Square(3,3,3,4),
                        Square(2,3,4,4)
                    ],
                    [
                        Square(3,4,1,3),
                        Square(2,4,2,3),
                        Square(1,4,3,4),
                        Square(4,4,4,4)
                    ]
                ]

        solver = Solver()
        actual = solver.solve(puzzle)

        for row in range(len(expected)):
            for column in range(len(expected)):
                self.assertEqual(expected[row][column].number, actual[row][column].number)
                self.assertEqual(expected[row][column].row, actual[row][column].row)
                self.assertEqual(expected[row][column].column, actual[row][column].column)
                self.assertEqual(expected[row][column].block, actual[row][column].block)

    def test_solve_9x9_grid(self):
        puzzle = [
                    [
                        Square(None,1,1,1),
                        Square(4,1,2,1),
                        Square(3,1,3,1),
                        Square(9,1,4,2),
                        Square(None,1,5,2),
                        Square(None,1,6,2),
                        Square(2,1,7,3),
                        Square(None,1,8,3),
                        Square(5,1,9,3)
                    ],
                    [
                        Square(8,2,1,1),
                        Square(None,2,2,1),
                        Square(5,2,3,1),
                        Square(None,2,4,2),
                        Square(7,2,5,2),
                        Square(None,2,6,2),
                        Square(6,2,7,3),
                        Square(None,2,8,3),
                        Square(None,2,9,3)
                    ],
                    [
                        Square(6,3,1,1),
                        Square(None,3,2,1),
                        Square(None,3,3,1),
                        Square(5,3,4,2),
                        Square(None,3,5,2),
                        Square(None,3,6,2),
                        Square(3,3,7,3),
                        Square(None,3,8,3),
                        Square(9,3,9,3)
                    ],
                    [
                        Square(None,4,1,4),
                        Square(None,4,2,4),
                        Square(2,4,3,4),
                        Square(None,4,4,5),
                        Square(8,4,5,5),
                        Square(None,4,6,5),
                        Square(None,4,7,6),
                        Square(None,4,8,6),
                        Square(None,4,9,6)
                    ],
                    [
                        Square(None,5,1,4),
                        Square(3,5,2,4),
                        Square(None,5,3,4),
                        Square(2,5,4,5),
                        Square(5,5,5,5),
                        Square(4,5,6,5),
                        Square(None,5,7,6),
                        Square(1,5,8,6),
                        Square(None,5,9,6)
                    ],
                    [
                        Square(None,6,1,4),
                        Square(None,6,2,4),
                        Square(None,6,3,4),
                        Square(None,6,4,5),
                        Square(1,6,5,5),
                        Square(None,6,6,5),
                        Square(9,6,7,6),
                        Square(None,6,8,6),
                        Square(None,6,9,6)
                    ],
                    [
                        Square(2,7,1,7),
                        Square(None,7,2,7),
                        Square(9,7,3,7),
                        Square(None,7,4,8),
                        Square(None,7,5,8),
                        Square(5,7,6,8),
                        Square(None,7,7,9),
                        Square(None,7,8,9),
                        Square(8,7,9,9)
                    ],
                    [
                        Square(None,8,1,7),
                        Square(None,8,2,7),
                        Square(4,8,3,7),
                        Square(None,8,4,8),
                        Square(2,8,5,8),
                        Square(None,8,6,8),
                        Square(5,8,7,9),
                        Square(None,8,8,9),
                        Square(7,8,9,9)
                    ],
                    [
                        Square(1,9,1,7),
                        Square(None,9,2,7),
                        Square(6,9,3,7),
                        Square(None,9,4,8),
                        Square(None,9,5,8),
                        Square(7,9,6,8),
                        Square(4,9,7,9),
                        Square(2,9,8,9),
                        Square(None,9,9,9)
                    ]
                ]

        expected = [
                    [
                        Square(7,1,1,1),
                        Square(4,1,2,1),
                        Square(3,1,3,1),
                        Square(9,1,4,2),
                        Square(6,1,5,2),
                        Square(1,1,6,2),
                        Square(2,1,7,3),
                        Square(8,1,8,3),
                        Square(5,1,9,3)
                    ],
                    [
                        Square(8,2,1,1),
                        Square(9,2,2,1),
                        Square(5,2,3,1),
                        Square(3,2,4,2),
                        Square(7,2,5,2),
                        Square(2,2,6,2),
                        Square(6,2,7,3),
                        Square(4,2,8,3),
                        Square(1,2,9,3)
                    ],
                    [
                        Square(6,3,1,1),
                        Square(2,3,2,1),
                        Square(1,3,3,1),
                        Square(5,3,4,2),
                        Square(4,3,5,2),
                        Square(8,3,6,2),
                        Square(3,3,7,3),
                        Square(7,3,8,3),
                        Square(9,3,9,3)
                    ],
                    [
                        Square(5,4,1,4),
                        Square(1,4,2,4),
                        Square(2,4,3,4),
                        Square(6,4,4,5),
                        Square(8,4,5,5),
                        Square(9,4,6,5),
                        Square(7,4,7,6),
                        Square(3,4,8,6),
                        Square(4,4,9,6)
                    ],
                    [
                        Square(9,5,1,4),
                        Square(3,5,2,4),
                        Square(7,5,3,4),
                        Square(2,5,4,5),
                        Square(5,5,5,5),
                        Square(4,5,6,5),
                        Square(8,5,7,6),
                        Square(1,5,8,6),
                        Square(6,5,9,6)
                    ],
                    [
                        Square(4,6,1,4),
                        Square(6,6,2,4),
                        Square(8,6,3,4),
                        Square(7,6,4,5),
                        Square(1,6,5,5),
                        Square(3,6,6,5),
                        Square(9,6,7,6),
                        Square(5,6,8,6),
                        Square(2,6,9,6)
                    ],
                    [
                        Square(2,7,1,7),
                        Square(7,7,2,7),
                        Square(9,7,3,7),
                        Square(4,7,4,8),
                        Square(3,7,5,8),
                        Square(5,7,6,8),
                        Square(1,7,7,9),
                        Square(6,7,8,9),
                        Square(8,7,9,9)
                    ],
                    [
                        Square(3,8,1,7),
                        Square(8,8,2,7),
                        Square(4,8,3,7),
                        Square(1,8,4,8),
                        Square(2,8,5,8),
                        Square(6,8,6,8),
                        Square(5,8,7,9),
                        Square(9,8,8,9),
                        Square(7,8,9,9)
                    ],
                    [
                        Square(1,9,1,7),
                        Square(5,9,2,7),
                        Square(6,9,3,7),
                        Square(8,9,4,8),
                        Square(9,9,5,8),
                        Square(7,9,6,8),
                        Square(4,9,7,9),
                        Square(2,9,8,9),
                        Square(3,9,9,9)
                    ]
                ]

        solver = Solver()
        actual = solver.solve(puzzle)

        for row in range(len(expected)):
            for column in range(len(expected)):
                self.assertEqual(expected[row][column].number, actual[row][column].number)
                self.assertEqual(expected[row][column].row, actual[row][column].row)
                self.assertEqual(expected[row][column].column, actual[row][column].column)
                self.assertEqual(expected[row][column].block, actual[row][column].block)

if __name__ == '__main__':
    unittest.main()
