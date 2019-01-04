import copy

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]

love = copy.deepcopy(grid)

for key in grid:
    for value in key:
        print(value, end="")
    print()

print()
print("==Love==")
print()

result = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
]

# iterate through rows
for i in range(len(love)):
    # iterate through columns
    for j in range(len(love[0])):
        result[j][i] = love[i][j]

for row in result:
    for columns in row:
        print(columns, end="")
    print()