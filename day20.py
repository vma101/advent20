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
inp = open_input(day)
# inp = open_sample(day)

class Tile:
    '''
    Tile class to represent a tile (a list of lists of "." and "#")
    '''
    def __init__(self, name, tile):
        self.name = name
        self.grid = np.array([[1 if loc == '#' else 0 for loc in row] for row in tile])
        # sides, need to be updated
        self.u = self.grid[0]
        self.d = self.grid[-1]
        self.l = self.grid[:, 0]
        self.r = self.grid[:, -1]
    
    def rot90(self):
        '''
        rotates grid to the LEFT by 90 deg
        '''
        self.grid = np.rot90(self.grid)
        self.updateSides()
        return self
    
    def fliplr(self):
        self.grid = np.fliplr(self.grid)
        self.updateSides()
        return self
    
    def flipud(self):
        self.grid = np.flipud(self.grid)
        self.updateSides()
        return self

    def updateSides(self):
        self.u = self.grid[0]
        self.d = self.grid[-1]
        self.l = self.grid[:, 0]
        self.r = self.grid[:, -1]
        return self
    
    def getSides(self):
        return [self.u, self.d, self.l, self.r]

    def getSide(self, side):
        sideDict = {
            'u': self.u,
            'd': self.d,
            'l': self.l,
            'r': self.r
        }
        return sideDict[side]

def processInp(inp):
    '''
    Create a dictionary with key as tile number, numpy arrays for the grid itself
    Create a second dictionary with edge arrays only, including flips (8 entries)

    Return: dictionary of key Tile, values Edges; dictionary of keys Edges, values int
    '''
    tileStart = 0
    tileSideDict = {}
    sideDict = {}
    tileDict = {}

    # create the tile Dictionaries
    
    for row in range(len(inp)):
        if inp[row] == '':
            tile = inp[tileStart: row]
            name = re.match('Tile ([0-9]+):', tile[0]).group(1)
            tileObj = Tile(name, tile[1:])
            tileDict[name] = tileObj
            tileSideDict[name] = tileObj.getSides()

            tileStart = row + 1
        elif row == len(inp) - 1:
            tile = inp[tileStart:]
            name = re.match('Tile ([0-9]+):', tile[0]).group(1)
            tileObj = Tile(name, tile[1:])
            tileDict[name] = tileObj
            tileSideDict[name] = tileObj.getSides()

    # create the side Dictionary
    
    for name in tileSideDict.keys():
        for side in tileSideDict[name]:
            sideKey = side.tobytes()
            if sideKey not in sideDict.keys():
                sideDict[sideKey] = 1
            elif sideKey in sideDict.keys():
                sideDict[sideKey] += 1

        flipSides = [np.flip(arr) for arr in tileSideDict[name]]
        tileSideDict[name].extend(side for side in flipSides)
        for side in flipSides:
            sideKey = side.tobytes()
            if sideKey not in sideDict.keys():
                sideDict[sideKey] = 1
            elif sideKey in sideDict.keys():
                sideDict[sideKey] += 1
                
    return tileSideDict, sideDict, tileDict

def task1(inp):
    '''
    Given raw input

    Return: corners of the eventual picture to be stitched
    '''
    tileSideDict, sideDict, _ = processInp(inp)
    tileMatch = {}
    tileMatchSum = {}
    for tile, sides in tileSideDict.items():
        tileMatch[tile] = [sideDict[side.tobytes()] for side in sides]
        tileMatchSum[tile] = sum(tileMatch[tile])

    sortedMatch = sorted(tileMatchSum.items(), key = lambda x:x[1])
    corners = sortedMatch[0:4]
    corners = [key for key, value in corners]
    task1ans = np.prod([int(x) for x in corners])
    return corners, task1ans, tileMatch

def arrTiles(cornerTile, tileDict, tileMatch, dim):
    '''
    Given a tile name meant to be the corner, a dictionary of Tile objects, and a
    dimension of the eventual picture for the tiles to be stitched in

    Return: numpy array of all the tile names
    '''
    if dim == None:
        dim = np.sqrt(len(tilesAll))

    tilesAll = [key for key in tileDict.keys()]
    tilesAll.remove(cornerTile)
    tileArr = np.empty([dim, dim], dtype = 'object')
    
    # orient the corner tile in such a way that two tiles can be adjoined to it
        # there are only 3 possible ways in which the tile can be oriented,
        # plus all the rotations from these sides
        # normal = [0, 1, 2, 3]
        # flipped u/d = [1, 0, 6, 7]
        # flipped l/r = [4, 5, 3, 2]
        # first figure out the ORIENTATION, then figure out the ROTATION allowing it to be topleft
    oriList = [[0, 1, 2, 3], [1, 0, 6, 7], [4, 5, 3, 2]]
    cornerMatches = np.array(tileMatch[cornerTile])
    cTile = tileDict[cTile]

    for i in range(len(oriList)):
        oriMatches = np.array(cornerMatches[oriList[i]])
        
        # case: normal orientation
        if i == 0:

            def rotArr(oriMatches, cTile):
                rotCount = 4
                cornerMatch = False
                while rotCount > 0:
                    # want the 2s (i.e. the matches) to be on the RIGHT, DOWN (i.e. index 1, 3 of oriList)
                    if [j for j in range(len(oriMatches)) if oriMatches[j] == 2] == [1, 3]:
                        cornerMatch = True
                        return cornerMatch
                    else:
                        cTile = cTile.rot90()
                        # top becomes left 0 --> 2
                        # bottom becomes right 1 --> 3
                        # left becomes bottom 2 --> 1
                        # right becomes top 3 --> 0
                        oriRot = {
                            0: 2,
                            1: 3,
                            2: 1,
                            3: 0
                        }
                        oriMatches = [oriMatches[oriRot[i]] for i in range(len(oriMatches))]
                        rotCount -= 1
                if not cornerMatch:
                    cTile = cTile.rot90()
                return cornerMatch, cTile
            
            
            cornerMatch, cTile = rotArr(oriMatches, cornerTile)
            if cornerMatch:
                break

        # case: flip up/down
        elif i == 1:
            cTile = cTile.flipud()
            cornerMatch, cTile = rotArr(oriMatches, cornerTile)
            
            if not cornerMatch:
                cTile = cTile.flipud()
            elif cornerMatch:
                break
            
        # case: flip left/right
        elif i == 2:
            cTile = cTile.fliplr()
            cornerMatch, cTile = rotArr(oriMatches, cornerTile)
            
            if not cornerMatch:
                cTile = cTile.fliplr()
            elif cornerMatch:
                break
    
    # after finding the corner tile, set it at the top-left corner of the array
    tileArr[0, 0] = cTile

    # at this point, the x, y = (0, 0) is already set, 
    for row in range(0, dim):
        for col in range(0, dim):
            # case: first row, not first column
            if row == 0 and col != 0:
                tile = tileArr[row, col - 1]
                for tileName in tilesAll:
                    otherTile = tileDict[tileName]
                    match, otherTile = oneTilePair(tile, 'r', otherTile)
                    if match:
                        tileArr[row, col] = otherTile
                        tilesAll.remove(tileName)
                        break

            # case: not first row, but first column
            elif row != 0 and col == 0:
                tile = tileArr[row - 1, col]
                for tileName in tilesAll:
                    otherTile = tileDict[tileName]
                    match, otherTile = oneTilePair(tile, 'd', otherTile)
                    if match:
                        tileArr[row, col] = otherTile
                        tilesAll.remove(tileName)

                        break
            
            # case: not first row, not first column
            elif row != 0 and col != 0:
                matchR = False
                rTile = tileArr[row, col - 1]
                matchD = False
                dTile = tileArr[row - 1, col]
                for tileName in tilesAll:
                    otherTile = tileDict[tileName]
                    matchR, otherTile = oneTilePair(rTile, 'r', otherTile)
                    matchD, otherTile = oneTilePair(dTile, 'd', otherTile)
                    if matchR and matchD:
                        tileArr[row, col] = otherTile
                        tilesAll.remove(tileName)
                        break
    return tileArr

def oneTilePair(tile, matchSide, otherTile):
    '''
    Given a tile object, the side to match it in, and another tile

    Return: reoriented tile object, and a boolean for matching
    '''
    ori = 3
    noMatch = False
    oppSide = {
        'd': 'u',
        'u': 'd',
        'l': 'r',
        'r': 'l'
    }
    tileSide = tile.getSide(matchSide)
    
    def rotMatch(tileSide, side, otherTile):
        # try all rotations
        match = False
        rotCount = 4
        while rotCount > 0:
            if all(tileSide == otherTile.getSide(side)):
                match = True
                break
            otherTile = otherTile.rot90()
            rotCount -= 1
        if match == False:
            otherTile = otherTile.rot90()
        return match, otherTile

    # try all rotations
    match, otherTile = rotMatch(tileSide, oppSide[matchSide], otherTile)

    # try flipping left/right
    if match == False:
        otherTile = otherTile.fliplr()
        match, otherTile = rotMatch(tileSide, oppSide[matchSide], otherTile)
    
    # try flipping up/down
    if match == False:
        otherTile = otherTile.flipud()
        match, othertile = rotMatch(tileSide, oppSide[matchSide], otherTile)

    return match, otherTile

def stitchTiles(tilesArr):
    '''
    Given an array of tile objects, stitch together after removing borders

    Return: an array of arrays of the stitched 'image'
    '''
    dim = tilesArr.shape[0]
    # stitchedGrid
    for row in range(dim):
        for col in range(dim):
            tile = tilesArr[row, col]
            if col == 0:
                tilesCol = tile.grid[1:-1, 1:-1]
            elif 0 < col < dim:
                tilesCol = np.concatenate((tilesCol, tile.grid[1: -1, 1: -1]), axis = 1)
            if col == dim - 1:
                if row == 0:
                    stitched = tilesCol
                elif row > 0:
                    stitched = np.concatenate((stitched, tilesCol), axis = 0)
    return stitched

coords = np.array([
    # row below
    (1, 1), (1, 4), (1, 7), (1, 10), (1, 13), (1, 16),
    # same row, ignore (0, 0)
    (0, 5), (0, 6), (0, 11), (0, 12), (0, 17), (0, 18), (0, 19),
    # row above
    (-1, 18)
])

def findMonsters(coords, stitched):
    '''
    Given the relative coordinates of a monster, and a stitched pattern

    Return: number of monsters
    '''
    # start with row 1, max out at len - 20
    count = 0
    for row in range(1, stitched.shape[0] - 1):
        for col in range(stitched.shape[1] - 20):
            if stitched[row, col] == 1:
                monster = oneMonster((row, col), coords, stitched)
                if monster:
                    count += 1
    return count

def oneMonster(loc, coords, stitched):
    '''
    Given a potential starting point for a monster, relative coordinates, and the stitched image

    Return: bool monster exists or not
    '''
    monster = True
    for adj in coords:
        adjLoc = np.array(loc) + np.array(adj)

        if stitched[adjLoc[0], adjLoc[1]] != 1:
            monster = False
            break
    return monster

def task2(coords, stitched):
    '''
    Given relative coordinates of a monster, and a stitched pattern

    Return: number of hashes in the image minus hashes in the monsters
    '''
    stitchedAll = sum(sum(stitched))
    count = 0
    
    # case: just rotation
    if count == 0:
        def rotFind(coords, stitched):
            rotCount = 4
            count = 0
            while rotCount >= 0 and count == 0:
                stitchedRot = np.rot90(stitched)
                count = findMonsters(coords, stitchedRot)
                if count > 0:
                    return count
                rotCount -= 1
            return count
        count = rotFind(coords, stitched)

    # case: flip up/down, rotate again
    if count == 0:
        stitchedud = np.flipud(stitched)
        count = rotFind(coords, stitchedud)

    # case: flip left/right, rotate again
    if count == 0:
        stitchedlr = np.fliplr(stitched)
        count = rotFind(coords, stitchedlr)
    return count, stitchedAll - count * (len(coords) + 1)

# Task Calls

## Task 1
# print(task1(inp))

## Task 2
corners, _, tileMatch = task1(inp)
_, _, tileDict = processInp(inp)
tilesArr = arrTiles(corners[0], tileDict, tileMatch, 12)
stitched = stitchTiles(tilesArr)
print(task2(coords, stitched))

