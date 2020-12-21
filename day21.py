'''
Advent of Code
Day 21: Allergen Assessment
https://adventofcode.com/2020/day/21

'''

day = 21
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
    Given raw input, parse each row for ingredients and contained allergens
    1. Create allerDict: allergen keys, possible ingredients as values
    2. Create ingrDict: ingredient keys, frequency of occurrence as values

    Return: allerDict, non-allergen containing ingredients, and their summed frequencies
    '''
    allerDict = {}
    ingrDict = {}
    allIngr = set()
    allerIngr = set()
    for row in inp:
        ingrRaw, allerRaw = re.match('([a-z\s]+) \(contains ([a-z\s,]+)\)', row).groups()
        ingrList = ingrRaw.split(" ")
        allerList = allerRaw.split(', ')
        for ingr in ingrList:
            allIngr.add(ingr)
            if ingr not in ingrDict.keys():
                ingrDict[ingr] = 1
            else:
                ingrDict[ingr] += 1
        for aller in allerList:
            if aller not in allerDict.keys():
                allerDict[aller] = {ingr for ingr in ingrList}
            else:
                newAllerSet = {ingr for ingr in ingrList}
                allerDict[aller] = allerDict[aller].intersection(newAllerSet)
    for allerKey, ingrVal in allerDict.items():
        for ingr in ingrVal:
            allerIngr.add(ingr)
    
    # ingredients not allergens
    nonAller = allIngr.difference(allerIngr)
    nonAllerCount = 0
    for ingr in nonAller:
        nonAllerCount += ingrDict[ingr]
    return allerDict, allIngr.difference(allerIngr), nonAllerCount

def oneIter(key, allerDict):
    '''
    Given a solved allergen key, an the allergen dictionary
    Subtract solved allergen-containing ingredient from all other sets in the allergen dictionary

    Return: updated allergen dictionary
    '''
    for allerKey, ingrList in allerDict.items():
        if allerKey != key:
            allerDict[allerKey] = allerDict[allerKey] - allerDict[key]
    return allerDict

def task2(allerDict):
    '''
    Given a dictionary of allergen keys to set of possible ingredients
    Solve for what ingredient contains the allergen

    Return: string of all ingredients corresponding to allergen keys sorted in alphabetical order
    '''
    solveCount = len(allerDict.keys())
    while solveCount > 0:
        for allerKey, ingrList in allerDict.items():
            if len(ingrList) == 1:
                solveCount -= 1
                allerDict = oneIter(allerKey, allerDict)
        if solveCount != 0:
            solveCount = len(allerDict.keys())
    azAller = sorted(allerDict)
    return ','.join([''.join(ingr for ingr in allerDict[aller]) for aller in azAller])


# Task Calls
# Task 1
print(task1(inp))
# Task 2
allerDict, _, _ = task1(inp)
print(task2(allerDict))