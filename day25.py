'''
Advent of Code
Day 25: Combo Breaker
https://adventofcode.com/2020/day/25

'''
day = 25
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
    Given public keys of card, door, and the transformation algorithm, determine the encryption key.

    Return: encryption key
    '''
    cardPub = int(inp[0])
    doorPub = int(inp[1])

    # Card Public Key assume first val = 1 (for loop size perform)
    # val = val * subject number (7)
    # set value to val % 20201227
    
    # Handshake
    # Get card public key
    # Get door public key
    # Transmit public keys to each other
    # Card: transform (subNum) door pubKey by its cardLoop - ENCRYPTION KEY
    # Door: transform (subNum) card pubKey by its doorLoop - ENCRYPTION KEY
        # kicker: the two encryption keys should match

    subNum = 7
    divNum = 20201227

    cardSize = 0
    card = 1
    while card != cardPub:
        cardSize += 1
        card = card * subNum
        card = card % divNum
    
    doorSize = 0
    door = 1
    while door != doorPub:
        doorSize += 1
        door = door * subNum
        door = door % divNum

    cardEnc = 1
    while cardSize > 0:
        cardSize -= 1
        cardEnc = cardEnc * doorPub
        cardEnc = cardEnc % divNum

    return cardEnc

print(task1(inp))

