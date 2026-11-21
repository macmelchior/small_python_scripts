'''
game_of_life.py
A simple implementation of John Conway's game of life. From Al Sweigart's "Automate the boring stuff with Python", with slight code edits on my side.
'''

import sys, random, time, copy
WIDTH = int(sys.argv[1])
HEIGHT = int(sys.argv[2])

print(WIDTH, HEIGHT)
 

# Create a list of cells
next_cells = []
# Generate cells randomly
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        column.append("#") if random.randint(0, 1) else column.append(" ")
    next_cells.append(column)

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(next_cells[x][y], end='')
    print()

# main while True loop
while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    # make a deep copy of next_cells and show on screen
    current_cells = copy.deepcopy(next_cells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')
        print()
    
    # Calculate cells for next steps
    # First, get coordinates of neighbors. We use % for wrapping.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            top = (y - 1) % HEIGHT
            bottom = (y + 1) % HEIGHT
            # Next, check neighboring cells
            num_of_neighbors = 0
            neighbors = [
                current_cells[left][top],
                current_cells[x][top],
                current_cells[right][top],
                current_cells[left][y],
                current_cells[right][y],
                current_cells[left][bottom],
                current_cells[x][bottom],
                current_cells[right][bottom],
            ]
            for neighbor in neighbors:
                if neighbor == "#":
                    num_of_neighbors += 1
            # Check if cell lives in next round
            if (current_cells[x][y] == "#" and 2 <= num_of_neighbors <= 3) or (current_cells[x][y] == " " and num_of_neighbors == 3):
                next_cells[x][y] = "#"
            else:
                next_cells[x][y] = " "
    time.sleep(1)


