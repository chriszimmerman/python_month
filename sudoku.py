import pprint

print('I can solve a sudoku grid of N * N. What is N?')
gridLength = int(input())

numbers = range(1, gridLength) 

grid = []
for i in range(0, gridLength):
    grid.append([])
    for j in range(0, gridLength):
        grid[i].append(j + 1)


for i in range(0, gridLength):
    for j in range(0, gridLength):
       print(str(grid[i][j]), end=" ") 
    print('')
