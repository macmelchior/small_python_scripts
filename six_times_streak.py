"""
six_times_streak.py
A small script which calculates the probability of throwing heads or tails 6 times in a row in a series of 100 throws. 
"""
import random


no_of_streaks = 0
for experiment_number in range(10000):
    throw_list = []
    for i in range(100):
        throw_list.append(random.choice(["H", "T"]))
    list_to_string = "".join(throw_list)
    if "HHHHHH" in list_to_string or "TTTTTT" in list_to_string:
        no_of_streaks += 1

print(f"Likelihood of 6-streak pass: {no_of_streaks / 100}%")