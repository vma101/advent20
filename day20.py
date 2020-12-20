'''
Advent of Code
Day 20: Jurassic Jigsaw
https://adventofcode.com/2020/day/20

'''

day = 20
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
# inp = open_input(day)
inp = open_sample(day)
# print(inp)

class Tile:
    def __init__(self, name, tile):
        self.name = name
        self.grid = np.array([[1 if loc == '#' else 0 for loc in row] for row in tile[1:]])
    
    def rot90(self):
        '''
        rotates grid to the LEFT by 90 deg
        '''
        self.grid = np.rot90(self.grid)
        return self.grid
    
    def fliplr(self):
        self.grid = np.fliplr(self.grid)
        return self.grid
    
    def flipud(self):
        self.grid = np.flipud(self.grid)

    def getSides(self):
        return [self.grid[0], self.grid[-1], self.grid[:, 0], self.grid[:, -1]]


def processInp(inp, part2 = False):
    '''
    Create a dictionary with key as tile number, numpy arrays for the grid itself
    Create a second dictionary with edge arrays only (4 entries)

    Return: dictionary of key Tile, values Edges; dictionary of keys Edges, values int
    '''
    tileStart = 0
    tileDict = {}
    sideDict = {}
    if not part2:
        for row in range(len(inp)):
            if inp[row] == '':
                tile = inp[tileStart: row]
                name = re.match('Tile ([0-9]+):', tile[0]).group(1)
                tileObj = Tile(name, tile[1:])
                tileDict[name] = tileObj.getSides()

                tileStart = row + 1
            elif row == len(inp) - 1:
                tile = inp[tileStart:]
                name = re.match('Tile ([0-9]+):', tile[0]).group(1)
                tileObj = Tile(name, tile[1:])
                tileDict[name] = tileObj.getSides()
        
        for name in tileDict.keys():
            for side in tileDict[name]:
                sideKey = side.tobytes()
                if sideKey not in sideDict.keys():
                    sideDict[sideKey] = 1
                elif sideKey in sideDict.keys():
                    sideDict[sideKey] += 1

            flipSides = [np.flip(arr) for arr in tileDict[name]]
            tileDict[name].extend(side for side in flipSides)
            for side in flipSides:
                sideKey = side.tobytes()
                if sideKey not in sideDict.keys():
                    sideDict[sideKey] = 1
                elif sideKey in sideDict.keys():
                    sideDict[sideKey] += 1
                
    # elif part2:
    #     for row in inp:
    #         if row == '':
    #             tile = inp[tileStart: row]
    #             name = re.match('Tile ([0-9]+):', tile[0]).group(1)
    #             tileDict[name] = Tile(name, tile[1:])
    #             tileStart = row + 1
    return tileDict, sideDict

# def oneTile(tile, tileDict, tileMatch):
#     matches = []
#     match = False
#     sides = tileDict[tile].getSides()
#     for side in sides:
#         for mTile in tileDict.keys():
#             if mTile != tile:
#                 # get the sides of the tile
#                 mSides = tileDict[tileName].getSides()
#                 for mSide in mSides:
#                     if all(side == mSide):
#                         matches.append(mTile)
#                         match = True
#                 match += tile
#     return tileMatch

def task(inp, part2 = False):
    tileDict, sideDict = processInp(inp)
    # within each value list, three possible orientations of the tile are possible
        # normal = [0:4]
        # flipped up/down = [0, 1, 6, 7] as LR would be flipped
        # flipped left/right = [2, 3, 4, 5] as UD would be flipped

        # get the MAXIMUM of matches for these orientations
    # oriList = [[0, 1, 2, 3], [0, 1, 6, 7], [2, 3, 4, 5]]
    tileMatch = {}
    for tile, sides in tileDict.items():
        tileMatch[tile] = sum([sideDict[side.tobytes()] for side in sides])
        # tileMatch[tile] = sum(tileMatch[tile])
        # tileMatch[tile] = sum([1 if x == 1 else 0 for x in tileMatch[tile]])
        # tileMatch[tile] = max([tileMatch[tile][ori].sum() for ori in oriList])

    
    sortedMatch = sorted(tileMatch.items(), key = lambda x:x[1])
    corners = sortedMatch[0:4]
    return sortedMatch, np.prod([int(key) for key, value in corners])

print(task(inp))
    