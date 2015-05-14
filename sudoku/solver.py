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

        for row in rows:
            values_from_squares = map(lambda x: x.number, row)
            numbers = list(filter(lambda x: x != None, values_from_squares))
            if self.__duplicate_numbers_in_row(numbers):
                return False

        for column in columns:
            values_from_squares = map(lambda x: x.number, column)
            numbers = list(filter(lambda x: x != None, values_from_squares))
            if self.__duplicate_numbers_in_row(numbers):
                return False
           
        for block in blocks:
            values_from_squares = map(lambda x: x.number, block)
            numbers = list(filter(lambda x: x != None, values_from_squares))
            if self.__duplicate_numbers_in_row(numbers):
                return False

        return True 
    

    def __duplicate_numbers_in_row(self, numbers):
        return len(numbers) != len(set(numbers))

