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

        file_reader = FileReader() 

        actual = file_reader.convert_file_lines_to_puzzle(lines_of_file)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
