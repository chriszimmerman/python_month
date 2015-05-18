class Solver():
    def is_valid(self, puzzle):
        return self.__check_for_uniqueness(puzzle, lambda x: x != None)

    def __check_for_uniqueness(self, puzzle, numberFilter):
        rows = []
        columns = []
        blocks = []

        for _ in puzzle:
            rows.append([])
            columns.append([])
            blocks.append([])

        for row in puzzle:
            for square in row:
                rows[square.row - 1].append(square)
                columns[square.column - 1].append(square)
                blocks[square.block - 1].append(square)

        return (self.__contains_unique_squares(rows, numberFilter)
            and self.__contains_unique_squares(columns, numberFilter)
            and self.__contains_unique_squares(blocks, numberFilter))

    def __contains_unique_squares(self, collections, numberFilter):
        for collection in collections:
            values_from_squares = map(lambda x: x.number, collection)
            numbers = list(filter(numberFilter, values_from_squares))
            if self.__duplicate_numbers_in_row(numbers):
                return False
        return True

    def __duplicate_numbers_in_row(self, numbers):
        return len(numbers) != len(set(numbers))

    def is_complete(self, puzzle):
        return self.__check_for_uniqueness(puzzle, lambda x: x == x)

    def solve(self, puzzle):
       return [[]] 
