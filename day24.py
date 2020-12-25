'''
Advent of Code
Day 24: 
https://adventofcode.com/2020/day/24

'''
day = 24
import re as re
import numpy as np

def open_input(day):
    with open("{}.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        # input_lists = np.array([list(row) for row in input])
    return inp

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        # input_lists = np.array([list(row) for row in input])
    return inp

### TOGGLE
inp = open_input(day)
# inp = open_sample(day)

def task1(inp):
    '''
    Given the instructions to flip a tile

    Return: set of tiles that are black by the end of the instructions, and corr. number
    '''
    blackSet = set()
    for row in inp:
        tileLoc = oneTile(row)
        if tileLoc in blackSet:
            blackSet.remove(tileLoc)
        else:
            blackSet.add(tileLoc)
    
    print(blackSet)
    
    return blackSet, len(blackSet)

def oneTile(row):
    '''
    Given the instructions to get to a tile

    Return: tuple of the tile's relative location
    '''
    # parse the row first:
    cur = 0
    # row, col
    tileLoc = [0, 0]
    while True:
        if row[cur] == "e":
            tileLoc[1] += 2
            cur += 1
        elif row[cur] == "w":
            tileLoc[1] -= 2
            cur += 1
        elif row[cur] == "s":
            if row[cur:cur + 2] == "se":
                tileLoc[0] -= 1
                tileLoc[1] += 1
            elif row[cur: cur + 2] == "sw":
                tileLoc[0] -= 1
                tileLoc[1] -= 1
            cur += 2
        elif row[cur] == "n":
            if row[cur:cur + 2] == "ne":
                tileLoc[0] += 1
                tileLoc[1] += 1
            elif row[cur: cur + 2] == "nw":
                tileLoc[0] += 1
                tileLoc[1] -= 1
            cur += 2
        
        if cur > len(row) - 1:
            break
    
    return tuple(tileLoc)

# List of immediately adjacent hex tile neighbors
adjList = [
    # east, west
    (0, 2), (0, -2),
    # north east, west
    (1, 1), (1, -1),
    # south east, west
    (-1, 1), (-1, -1)
]

def oneDay(blackSet):
    '''
    Given instructions on what tiles to flip in one iteration

    Return: new set of black tiles at the end of the day
    '''
    blackSetNew = set()
    whiteSetCheck = set()
    adjBlack = 0
    adjWhite = 0
    # iterate through all the current black tiles to see if they stay black
    for tileLoc in blackSet:
        for incr in adjList:
            adjLoc = tuple([tileLoc[0] + incr[0], tileLoc[1] + incr[1]])

        # if existing tile is black, then check neighbors to see if adj Black = 1 or 2
            if adjLoc in blackSet:
                adjBlack += 1
            # if existing tile is white, add to white squares to check
            else:
                whiteSetCheck.add(adjLoc)

        if 0 < adjBlack <= 2:
            blackSetNew.add(tileLoc)
        adjBlack = 0
    
    for tileLoc in whiteSetCheck:
        for incr in adjList:
            adjLoc = tuple([tileLoc[0] + incr[0], tileLoc[1] + incr[1]])
            if adjLoc in blackSet:
                adjWhite += 1
        if adjWhite == 2:
            blackSetNew.add(tileLoc)
        adjWhite = 0

    return blackSetNew

def task2(inp, days = 100):
    '''
    Given instructions on what tiles to flip on the first day, how many days to iterate

    Return: length of black tiles at the end of given timeframe
    '''
    blackSet, blackCount = task1(inp)
    while days > 0:
        blackSet = oneDay(blackSet)
        days -= 1
    
    return len(blackSet)

# print(task1(inp))
print(task2(inp))