import unittest
from file_reader import FileReader
from square import Square

class FileReaderTest(unittest.TestCase):
    def test_convert_file_lines_to_puzzle(self):
        lines_of_file = [
                            '1 2 3 4\n',
                            '2 3 4 1\n',
                            '3 4 1 2\n',
                            '4 1 2 3\n'
                        ]
        expected = [
                    [
                        Square(1,1,1,1),
                        Square(2,1,2,1),
                        Square(3,1,3,2),
                        Square(4,1,4,2)
                    ],
                    [
                        Square(2,2,1,1),
                        Square(3,2,2,1),
                        Square(4,2,3,2),
                        Square(1,2,4,2)
                    ],
                    [
                        Square(3,3,1,3),
                        Square(4,3,2,3),
                        Square(1,3,3,4),
                        Square(2,3,4,4)
                    ],
                    [
                        Square(4,4,1,3),
                        Square(1,4,2,3),
                        Square(2,4,3,4),
                        Square(3,4,4,4)
                    ]
                ]

        file_reader = FileReader() 

        actual = file_reader.convert_file_lines_to_puzzle(lines_of_file)

        for i in range(4):
            for j in range(4):
                self.assertEqual(expected[i][j].number, actual[i][j].number)
                self.assertEqual(expected[i][j].row, actual[i][j].row)
                self.assertEqual(expected[i][j].column, actual[i][j].column)
                self.assertEqual(expected[i][j].block, actual[i][j].block)

if __name__ == '__main__':
    unittest.main()
