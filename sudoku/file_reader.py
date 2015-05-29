import pprint
import os
import math
from square import Square

class FileReader:
    def get_puzzle_from_file(self, filename):
        lines = self.__read_from_file(filename)
        return self.__convert_file_lines_to_puzzle(lines)

    def __read_from_file(self, filename):
        filepath = os.getcwd() + '/' + filename

        try:
            file = open(filepath)
            lines = file.readlines()
            file.close()

            return lines
        except IOError:
            print("The file could not be found or is not in the right format.")

    def __convert_file_lines_to_puzzle(self, lines):
        lines = list(map(lambda line: line.strip(), lines))
        lines = list(map(lambda line: line.split(' '), lines))

        puzzle = []
        puzzleLength = len(lines)

        for row in range(puzzleLength):
            currentRow = []
            for column in range(puzzleLength):
                number = int(lines[row][column]) if lines[row][column].isdigit() else None
                new_square = Square(number, row + 1, column + 1, self.__calculate_block(row + 1, column + 1, puzzleLength))
                currentRow.append(new_square)
            puzzle.append(currentRow)

        return puzzle

    def __calculate_block(self, row, column, puzzleLength):
        puzzleLengthSqrt= math.sqrt(float(puzzleLength))
        return int(math.floor(float(row - 1) / float(puzzleLengthSqrt)) * puzzleLengthSqrt) + math.ceil(float(column) / float(puzzleLengthSqrt));
