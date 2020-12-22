'''
Advent of Code
Day 22: Crab Combat
https://adventofcode.com/2020/day/22

'''
day = 22
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

def processInp(inp):
    '''
    processes input into players' respective decks

    Returns: dictionary of player Keys to list of cards Values
    '''
    playerDict = {}
    for row in range(len(inp)):
        if inp[row] == "":
            player1, player2 = inp[:row], inp[row + 1:]
            playerDict[re.match('Player ([0-9]+):', player1[0]).group(1)] = [int(num) for num in player1[1:]]
            playerDict[re.match('Player ([0-9]+):', player2[0]).group(1)] = [int(num) for num in player2[1:]]

    return playerDict

def oneRound(p1, p2):
    '''
    plays 1 round of Combat

    returns: bool for player 1 win
    '''
    p1Win = False
    if p1 > p2:
        p1Win = True
    elif p2 > p1:
        p1Win = False
    return p1Win

def task1(inp):
    '''
    Plays 1 game of Combat

    Returns: number of rounds to win, sum over (winning card * position i in hand)
    '''
    playerDict = processInp(inp)
    ps = [p for p in playerDict.keys()]
    empty = False
    roundCount = 0
    while not empty:
        p1, p2 = [playerDict[p].pop(0) for p in ps]
        p1Win = oneRound(p1, p2)
        if p1Win:
            playerDict['1'].extend([p1, p2])
        else:
            playerDict['2'].extend([p2, p1])

        # check to see if the game is over
        if not empty:
            if playerDict['1'] == []:
                winDeck =  np.array(playerDict['2'][::-1])
                empty = True
                break
            elif playerDict['2'] == []:
                winDeck = np.array(playerDict['1'][::-1])
                empty = True
                break
            else:
                roundCount += 1

    winSum = np.multiply(winDeck, range(1, len(winDeck) + 1))
    return roundCount, sum(winSum)


def oneGame(playerDict):
    '''
    Plays one game of Recursive Combat

    Returns: dictionary of players and ending hands, boolean for whether player 1 wins
    '''
    p1Win = False
    empty = False
    ps = [p for p in playerDict.keys()]

    # prepare the hash list
    p1Hash = hash(tuple(playerDict['1']))
    p2Hash = hash(tuple(playerDict['2']))
    roundList = [(p1Hash, p2Hash)]

    roundCount = 1
    while not empty:
        # get deal card values
        p1, p2 = [playerDict[p].pop(0) for p in ps]
        
        # hash the two decks
        p1Hash = hash(tuple(playerDict['1']))
        p2Hash = hash(tuple(playerDict['2']))
        
        # case: if the round has already been played before, winner is player 1
        if tuple([p1Hash, p2Hash]) in roundList or tuple([p2Hash, p1Hash]) in roundList:
            # player 1 wins
            p1Win = True
            empty = True
            return playerDict, p1Win

        # case: if the round has NOT been played before
        else:
            # add the round to the roundList
            roundList.append((p1Hash, p2Hash))

            # if both players have more cards than the card they just drew, recurse
            if len(playerDict['1']) >= p1 and len(playerDict['2']) >= p2:
                # recurse
                subDict = {}
                subDict['1'] = playerDict['1'][:p1]
                subDict['2'] = playerDict['2'][:p2]
                subDict, p1Win, roundDict = oneGame(subDict, roundDict)

            # if at least 1 player does not have enough cards to recurse, play a round
            else:
                p1Win = oneRound(p1, p2)
                
        # if p1Win, regardless of if early truncation, recursed, or normal round
        if p1Win:
            playerDict['1'].extend([p1, p2])
        else:
            playerDict['2'].extend([p2, p1])

        # check to see if the game is over
        if not empty:
            if playerDict[ps[0]] == [] or playerDict[ps[1]] == []:
                empty = True
                break
            else:
                roundCount += 1
    
    return playerDict, p1Win

def task2(inp):
    '''
    Play 1 game of recursive combat with the input

    Return: sum over (winning card * position i in hand)
    '''
    playerDict = processInp(inp)
    
    empty = False
    playerDict, p1Win, _ = oneGame(playerDict)
    if p1Win:
        winDeck = np.array(playerDict['1'][::-1])
    else:
        winDeck = np.array(playerDict['2'][::-1])
    winSum = np.multiply(winDeck, range(1, len(winDeck) + 1))
    return sum(winSum)

# Task Calls
print(task1(inp))
# print(task2(inp))

            