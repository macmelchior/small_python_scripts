"""
matrix.py
Cool colored matrix-like effect in the terminal. Based on an exercise from Al Sweigart's book "Automate the boring stuff with Python".
"""

import random, sys, time
DEFAULT_COLOR = "\033[0m"
GREEN = "\033[32m"
WIDTH = 100

def matrix():
    # Initialize with all columns == 0
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            # On random interval, change the value of random column to random number between 5 and 10
            if random.randint(0, 20) == 5:
                columns[random.randint(0, WIDTH-1)] = random.randint(5, 10)
            # If colum value equals 0, print empty space
            if columns[i] == 0:
                print(" ", end = "")
            else:
                # Choose random character and print in green. Decrease column value.
                char = random.choice(["○", "●"])
                print(f"{GREEN}{char}", end = "")
                columns[i] -= 1
        # Change back to default color at the end of the line
        print(f"{DEFAULT_COLOR}")
        time.sleep(0.1)
                

def main():
    try:
        matrix()
    except KeyboardInterrupt:
        sys.exit()
    

if __name__ == "__main__":
    main()
