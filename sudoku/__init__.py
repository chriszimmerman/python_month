from solver import Solver
from file_reader import FileReader

filename = input("Enter your puzzle file:")

file_reader = FileReader()
file_contents = file_reader.read_from_file(filename)
puzzle = file_reader.convert_file_lines_to_puzzle(file_contents)

solver = Solver()

if solver.is_valid(puzzle):
    print("Okay, I can solve this.")
else:
    print("This puzzle is invalid.")
    
