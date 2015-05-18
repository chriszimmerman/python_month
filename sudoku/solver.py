class Solver():
    def is_valid(self, puzzle):
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

        return ( self.__contains_unique_squares(rows)
            and self.__contains_unique_squares(columns)
            and self.__contains_unique_squares(blocks))

    def __contains_unique_squares(self, collections):
        for collection in collections:
            values_from_squares = map(lambda x: x.number, collection)
            numbers = list(filter(lambda x: x != None, values_from_squares))
            if self.__duplicate_numbers_in_row(numbers):
                return False
        return True

    def __duplicate_numbers_in_row(self, numbers):
        return len(numbers) != len(set(numbers))

    def is_complete(self, puzzle):
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

        return ( self.__contains_unique_squares_not_filtering_blanks(rows)
            and self.__contains_unique_squares_not_filtering_blanks(columns)
            and self.__contains_unique_squares_not_filtering_blanks(blocks))

    def __contains_unique_squares_not_filtering_blanks(self, collections):
        for collection in collections:
            numbers = list(map(lambda x: x.number, collection))
            if self.__duplicate_numbers_in_row(numbers):
                return False
        return True

    def solve(self, puzzle):
       return [[]] 
