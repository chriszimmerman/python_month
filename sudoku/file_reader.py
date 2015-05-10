import pprint
import os
from square import Square

class FileReader:

    def read_from_file(self, filename):
        filepath = os.getcwd() + '/' + filename

        try:
            file = open(filepath)
            lines = file.readlines()
            file.close()

            return lines
        except IOError:
            print("The file could not be found or is not in the right format")

    def convert_file_lines_to_puzzle(self, lines):
        lines = list(map(lambda line: line.strip(), lines))
        lines = list(map(lambda line: line.split(' '), lines))

        squares = []
        for line in lines:
            for i in range(len(line)):
                number = int(line[i])
                line[i] = Square(number, lines.index(line) + 1, i + 1, i + 1)
            squares.append(line)

        return squares
