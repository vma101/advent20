'''
Advent of Code
Day 15: Rambunctious Recitation
https://adventofcode.com/2020/day/15

'''

day = 15
import re as re
import numpy as np

### TOGGLE
inp = np.array([2,20,0,4,1,17])
# Testing inputs
# inp = np.array([0, 3, 6])
# inp = np.array([1, 3, 2])
# inp = np.array([2, 1, 3])
# inp = np.array([1, 2, 3])
# inp = np.array([2, 3, 1])
# inp = np.array([3, 2, 1])
# inp = np.array([3, 1, 2])

def oneTurn(i, turn_val, turns):
    if turn_val in turns.keys():
        turns[turn_val].append(i)
    else:
        turns[turn_val] = [i]
    return turns

def task1(inp, end = 30000000):
    turn_vals = []
    turn_val = 0
    turns = {}
    for i in range(end):
        if i < len(inp):
            turn_val = inp[i]
            
        elif turn_val in turns.keys():
            # last value said was for the first time
            if len(turns[turn_val]) == 1:
                turn_val = 0

            else:
                turn_val = turns[turn_val][-1] - turns[turn_val][-2]
        turns = oneTurn(i, turn_val, turns)
        turn_vals.append(turn_val)
        # print(turn_val)
    return turn_val

# Task Calls
print(task1(inp, 2020))
print(task1(inp))
        



        
