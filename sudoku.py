import pprint
import os

print('I can solve a sudoku grid of N^2 * N^2. What is N?')
gridLength = int(input())

numbers = range(1, gridLength) 

print('What is the name of the file? It must be in the same directory as this script.')
filename = input()
filepath = os.getcwd() + '/' + filename

if os.path.exists(filepath):
    file = open(filepath)
    lines = file.readlines()
    lines = list(map(lambda line: line.strip(), lines))
    lines = list(map(lambda line: line.split(' '), lines))

    for line in lines:
        for i in range(len(line)):
            line[i] = int(line[i])
    file.close()

    grid = lines
else:
    print('Invalid filename.')
    sys.exit(0)

print(grid)
