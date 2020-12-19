'''
Advent of Code
Day 2: Password Philosophy
https://adventofcode.com/2020/day/2

'''

import pandas as pd
import numpy as np

with open("2.txt", "r") as entries:
    inp = [entry.rstrip("\n") for entry in entries]

valid_count = 0

def task1(inp):
    '''
    Given a list of strings with the structure
    < rule > < letter > : < password >
    < rule > stipulates the number of times that < letter > can appear in < password >
    
    Return: number of passwords that are valid according to the rule imposed
    '''
    for i in range(len(inp)):
        low = int(inp[i][:inp[i].find('-')])
        high = int(inp[i][inp[i].find('-')+1:inp[i].find(' ')])
        letter = inp[i][inp[i].find(' ')+1]
        password = inp[i][inp[i].find(':')+2:]
        letter_count = sum(map(lambda x : 1 if letter in x else 0, password))
        if letter_count >= low and letter_count <= high:
            valid_count += 1
            print(password)
    return valid_count

def task2(inp):
    '''
    Given a list of strings with the structure
    < rule > < letter > : < password >
    < rule > stipulates the positions that < letter > must appear in < password > in EITHER / OR fashion

    Return: number of passwords that are valid according to the rule imposed
    '''
    valid_count = 0
    valid = 0

    for i in range(len(inp)):
        pos1 = int(inp[i][:inp[i].find('-')]) - 1
        pos2 = int(inp[i][inp[i].find('-')+1:inp[i].find(' ')]) - 1
        letter = inp[i][inp[i].find(' ')+1]
        password = inp[i][inp[i].find(':')+2:]
        if password[pos1] == letter and password[pos2] != letter:
            valid = 1
        elif password[pos1] != letter and password[pos2] == letter:
            valid = 1
        if valid == 1:
            valid_count += 1
            valid = 0
    return valid_count