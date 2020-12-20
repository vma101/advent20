'''
Advent of Code
Day 17: Conway Cubes
https://adventofcode.com/2020/day/17

'''
day = 17
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

def adjSet(dim = 3):
    '''
    Create a set of neighbors, 3D
    Note - this array includes self - (0, 0, 0)
    '''
    adjRange = np.array([-1, 0, 1])
    xyAdj = np.array([
        # same row
        (0, -1), (0, 0), (0, 1),
        # row above
        (1, -1), (1, 0), (1, 1),
        # row below
        (-1, -1), (-1, 0), (-1, 1)
    ])
    zAdj = np.array([-1, 0, 1])
    wAdj = np.array([-1, 0, 1])

    adjIncr = []

    if dim == 3:
        for z in zAdj: 
            for xy in xyAdj: 
                adjIncr.append(tuple([xy[0], xy[1], z]))
                # print('neighbor block', adjIncr)

    elif dim == 4:
        for w in wAdj:
            for z in zAdj: 
                for xy in xyAdj: 
                    adjIncr.append(tuple([xy[0], xy[1], z, w]))
                    # print('neighbor block', adjIncr)
    return adjIncr

def processInp(inp, dim = 3):
    '''
    Process input to create first active set
    '''
    activeSet = set()
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            if inp[row][col] == '#':
                newTup = [0] * dim
                newTup[0] = row
                newTup[1] = col
                activeSet.add(tuple(newTup))
    return activeSet

def oneRound(activeSet):
    '''
    First create a list of locations that need to be traversed
    Second traverse locations one at a time

    Return new set of active locations
    '''
    locList = set()
    adjIncr = adjSet()
    for loc in activeSet:
        for adj in adjIncr:
            neighborLoc = np.array(loc) + np.array(adj)
            locList.add(tuple(neighborLoc))
    
    activeSetNew = set()
    for loc in locList:
        activeSetNew = oneCube(loc, activeSet, activeSetNew)

    return activeSetNew

def oneCube(loc, activeSet, activeSetNew, locState = 0, dim = 3):
    activeAdj = 0
    adjIncr = adjSet()
    adjIncr.remove(tuple([0] * dim))

    for adj in adjIncr:
        nLoc = np.array(loc) + np.array(adj)
        if tuple(nLoc) in activeSet:
            activeAdj += 1
    
    # if inactive, check to see if exactly 3 neighbors are active
    if loc not in activeSet:
        if activeAdj == 3:
            activeSetNew.add(loc)
            
        
    # if active, check to see if exactly 2 - 3 neighbors are active
    elif loc in activeSet:
        if 2 <= activeAdj <= 3:
            activeSetNew.add(loc)

    return activeSetNew

def task1(inp, rounds = 6):
    activeSet = processInp(inp)
    # print('called on', activeSet)
    round = 0
    while round < rounds:
        activeSet = oneRound(activeSet)
        # print('returning', activeSet)
        round += 1
    return activeSet, len(activeSet)

print(task1(inp))
print(task1(inp, 4))

