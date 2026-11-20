"""
door_mat.py
Solution to one of the hacker rank challenges:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be X. ( is an odd natural number, and is times .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

"""

height, width = map(int, input().split())
center_row = height // 2

def print_line(i):
    symbols = i * ".|."
    dashes = (width - len(symbols)) // 2
    dashes *= "-"
    print(f"{dashes}{symbols}{dashes}")

for i in range(1, height, 2):
    print_line(i)
print(f'{"-" * ((width - len("WELCOME"))//2)}WELCOME{"-" * ((width - len("WELCOME"))//2)}')
for i in range(height - 2, 1, - 2):
    print_line(i)