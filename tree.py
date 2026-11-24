"""
tree.py
Just a small script to practice working on 2-D matrices
"""

tree = [
    [".", ".", ".", ".", ".", "X", " ", "M"],
    [".", ".", ".", ".", "X", "X", " ", "E"],
    [".", ".", ".", "X", "X", "O", " ", "R"],
    [".", ".", "X", "X", "O", "X", " ", "R"],
    [".", "X", "O", "X", "X", "X", "|", "Y"],
    ["X", "X", "X", "X", "X", "X", " ", " "],
    [".", "X", "X", "O", "X", "X", "|", "X"],
    [".", ".", "X", "X", "X", "O", " ", "-"],
    [".", ".", ".", "X", "X", "X", " ", "M"],
    [".", ".", ".", ".", "X", "X", " ", "A"],
    [".", ".", ".", ".", ".", "X", " ", "S"],
]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end="")
    print()