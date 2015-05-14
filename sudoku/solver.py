class Solver():
    def is_valid(self, puzzle):
        for row in puzzle:
            values_from_squares = map(lambda x: x.number, row)
            numbers = list(filter(lambda x: x != None, values_from_squares))
            if self.__duplicate_numbers_in_row(numbers):
                return False
        return True 
    

    def __duplicate_numbers_in_row(self, numbers):
        return len(numbers) != len(set(numbers))

