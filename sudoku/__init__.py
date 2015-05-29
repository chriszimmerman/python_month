import sys
from solver import Solver
from file_reader import FileReader

if len(sys.argv) != 2:
    print("Please specify a puzzle file to solve.")
    sys.exit(0)

filename = sys.argv[1]
file_reader = FileReader()

puzzle = file_reader.get_puzzle_from_file(filename)

solver = Solver()

if solver.is_valid(puzzle):
    print('Okay, I can solve this.')
    solution = solver.solve(puzzle)

    for row in solution:
        for square in row:
            print(str(square.number) + ' ', end='')
        print('\n', end='')
else:
    print('This puzzle is invalid.')
    
