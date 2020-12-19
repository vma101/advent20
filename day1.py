'''
Advent of Code
Day 1: Report Repair
https://adventofcode.com/2020/day/1

'''
import pandas as pd
import numpy as np

with open("1.txt", "r") as entries:
    inp = [int(entry.rstrip("\n")) for entry in entries]


def task1(inp, target = 2020):
    '''
    Given a list of input numbers, find 2 that sum to the target
    Return: product of the 2 numbers
    '''
    done = 0
    while done == 0:
        for i in range(len(inp)):
            for j in range(len(inp)):
                if i != j:
                    # print(inp[i], inp[j], inp[i] + inp[j])
                    if (inp[i] + inp[j]) == 2020:
                        print("final answer: {}, {}, multiplied = {}".format(inp[i], inp[j], inp[i]*inp[j]))
                        done = 1
    return inp[i] * inp[j]

def task2(inp):
    '''
    Given a list of input numbers, find 3 that sum to the target
    Return: product of the 3 numbers
    '''
    done = 0
    while done == 0:
        for i in range(len(inp)):
            for j in range(len(inp)):
                for k in range(len(inp)):
                    if i != j and j != k and i != k:
                        sum_ijk = inp[i] + inp[j] + inp[k]
                        # print(inp[i], inp[j], inp[k], inp[i] + inp[j] + inp[k])
                        if sum_ijk == 2020:
                            print("final answer: {}, {}, {}, multiplied = {}".format(inp[i], inp[j], inp[k], inp[i]*inp[j]*inp[k]))
                            done = 1
    return inp[i]*inp[j]*inp[k]