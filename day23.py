'''
Advent of Code
Day 23: 
https://adventofcode.com/2020/day/23

'''
day = 23
import re as re
import numpy as np
import bisect

### TOGGLE
inp = [int(num) for num in '219347865']
# inp = [int(num) for num in '389125467']

## List Implementation - Unideal, very slow

def oneMove(inp, currId):

    currCup = inp[currId]
    # print('called on', currCup, 'in', inp)

    # picks up 3 cups immediately clockwise of current cup, REMOVED
    pickUpId = []
    for i in range(1,4):
        if currId + i < len(inp):
            pickUpId.append(currId + i)
        else:
            pickUpId.append(currId + i - len(inp))
    pickUp = [inp[idx] for idx in pickUpId]
    # print('pick up', pickUp)
    for val in pickUp:
        inp.remove(val)

    # selects destination cup - label = current cup label - 1; keep subtracting until achieved, or wrap to highest
    subCups = inp[:]
    subCups.remove(currCup)
    destCup = 0
    minCup = min(subCups)
    dest = False
    decr = 1
    while not dest:
        if (currCup - decr) in inp:
            destCup = currCup - decr
            dest = True
            break
        elif (currCup - decr) < minCup:
            destCup = max(subCups)
            dest = True
            break
        else:
            decr += 1
    # print('destination cup', destCup)
        
    # insert cups clockwise of destination cup
    idx = inp.index(destCup) + 1
    for cup in pickUp:
        inp.insert(idx, cup)
        idx += 1
    
    newId = inp.index(currCup)
    if currId != newId:
        shift = currId - newId
        inp = np.roll(inp, shift)
    return list(inp)

def task1(inp, moves = 100):
    currId = 0
    while moves > 0:
        inp = oneMove(inp, currId)
        moves -= 1
        currId += 1
        if currId == len(inp):
            currId = 0
    
    oneId = inp.index(1)
    inpOne = np.roll(inp, 0 - oneId)
    return ''.join([str(num) if num != 1 else '' for num in list(inpOne)])

def task2(inp, moves = 1000000):
    inpAdd = list(np.arange(max(inp) + 1, moves + 1))
    inp = inp + inpAdd
    # print(len(inp))

    currId = 0
    while moves > 0:
        if moves % 1000 == 0:
            print('move', moves)
        inp = oneMove(inp, currId)
        moves -= 1
        currId += 1
        if currId == len(inp):
            currId = 0

    oneId = inp.index(1)
    twoCups = inp[oneId + 1: oneId + 3]
    return np.prod(twoCups)

## Linked List Implementation
class LinkedList:
    '''
    Linked list class and functions:

    1) Create the master linked list object
    2) Create a dictionary of node values pointing to nodes, each node is really a linked list object
    3) Pick up 3 cups clockwise of current node, return the list and corr values
    4) Insert the 3 cups clockwise of the destination node
    5) Print the string of all nodes following given node
    '''

    def __init__(self, val):
        self.v = val
        self.next = self
    
    @classmethod
    def createList(cls, valList):
        head = cls(valList[0])
        cur = head

        for i in range(1, len(valList)):
            node = cls(valList[i])
            cur.next = node
            cur = node
        
        cur.next = head
        return head
    
    def createNodeDict(self):
        nodeDict = {}
        node = self
        head = self
        
        while True:
            nodeDict[node.v] = node
            node = node.next
            if node == head:
                break
        
        return nodeDict

    def pickUp(self, num = 3):
        pickUpHead = self.next
        pickUpEnd = pickUpHead
        pickUpVal = [pickUpEnd.v]

        for i in range(1, num):
            pickUpEnd = pickUpEnd.next
            pickUpVal.append(pickUpEnd.v)   
        
        self.next = pickUpEnd.next
        pickUpEnd.next = None

        return pickUpHead, pickUpVal
    
    def insertCups(self, pickUpHead):
        nodeAfter = self.next
        self.next = pickUpHead

        while pickUpHead.next:
            pickUpHead = pickUpHead.next
        
        pickUpHead.next = nodeAfter
    
    def to_str(self):
        head = self
        cur = head
        valList = []
        while True:
            valList.append(f'{cur.v}')
            cur = cur.next

            if cur == head:
                break
        return ''.join(valList)

def crabCups(inp, moves = 10000000, task2 = True):
    '''
    Play the game given the input cups, number of moves to run.
    If task1: take input as is
    If task2: append ascending cups of 10 - 1mil after existing input

    Return: 
    If task1: string of cups after 1
    If task2: product of the labels on the 2 cups after label 1
    '''
    if task2:
        inp += [num for num in range(max(inp) + 1, 1000001)]
    
    origCups = LinkedList.createList(inp)
    cups = origCups
    minCup, maxCup = min(inp), max(inp)
    cupDict = cups.createNodeDict()

    while moves > 0:
        # get value of current cup
        
        currCup = cups.v

        # remove 3 cups next to current cup
        pickUpHead, pickUpCups = cups.pickUp(3)

        # figure out what the destination cup should be
        destCup = currCup - 1
        while destCup not in cupDict or destCup in pickUpCups:
            destCup -= 1
            if destCup < minCup:
                destCup = maxCup

        # if moves % 100000 == 0:
        #     print(currCup, pickUpCups, destCup)
        
        # insert 3 cups next to the destination cup
        cupDict[destCup].insertCups(pickUpHead)
        cups = cups.next
        moves -= 1

    if task2:
        oneCup = cupDict[1]
        twoCups = [oneCup.next.v, oneCup.next.next.v]
        print(twoCups)
        print(cupDict[934001].next.v)
        # print(cups.to_str())
        return np.prod(twoCups)

    else:
        return cupDict[1].next.to_str()[:-1]

# Task Calls

## First 2 rely on a non-linked list, no dictionary method, not advised!
# print(task1(inp))
# print(task2(inp))

## Uses a linked list!
print(crabCups(inp, 100, False))
print(crabCups(inp))