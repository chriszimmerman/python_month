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
        length = len(puzzle)
        already_solved_squares = []
        potentially_solved_squares = []
        squares_to_solve = []
        backtrack_stack = []
    
        for row in puzzle:
            for square in row:
                if square.number == None:
                    squares_to_solve.append(square)
                else:
                    already_solved_squares.append(square)

        take_from_potential_solution = False
        square_tried = False
       
        while len(squares_to_solve) > 0 or len(backtrack_stack) > 0:
            if take_from_potential_solution and len(potentially_solved_squares) > 0:
                current_square = potentially_solved_squares.pop()
            elif len(backtrack_stack) > 0: 
                current_square = backtrack_stack.pop()
            else:
                current_square = squares_to_solve.pop()

            if current_square.number == None:
                current_square.number = 0

            for _ in range(length):
                current_square.number = current_square.number % length + 1
            
                if self.is_valid(puzzle): 
                    potentially_solved_squares.append(current_square)
                    take_from_potential_solution = False
                    square_tried = True
                    break
               
            if not square_tried:
                backtrack_stack.append(current_square)
                take_from_potential_solution = True 
                square_tried = False

        return puzzle 
