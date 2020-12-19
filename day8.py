'''
Advent of Code
Day 8: Handheld Halted
https://adventofcode.com/2020/day/8

'''

day = 8
import re as re

def open_inp(day):
    with open("{}.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
    return inp

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
    return inp

### TOGGLE
inp = open_inp(day)
# inp = open_sample(day)

def execute_step(inp, i, counter):
    '''
    Given one step, execute it.
    
    Return: next step to execute, and updated counter
    '''
    instru = inp[i].split(" ")[0]
    num = int(inp[i].split(" ")[1])
    if instru == "jmp":
        next_i = i + num
    elif instru == "acc":
        next_i = i + 1
        counter += num
    elif instru == "nop":
        next_i = i + 1
    print(i, instru, next_i, counter)
    return next_i, counter

def run_all(inp):
    '''
    Given a list of steps, execute them until a step repeats.

    Return: the next command to execute, counter
    '''
    counter = 0
    inp_track = set()
    next_i = 0
    for i in range(len(inp)):
        if i == 0 and counter == 0:
            next_i = i
        while (next_i not in inp_track):
            if next_i == (len(inp)):
                return next_i, counter
            inp_track.add(next_i)
            next_i, counter = execute_step(inp, next_i, counter)  
    return next_i, counter

def run_all_caveat(inp):
    '''
    Given a list of steps, execute them until the last step is reached.
    Try substituting 'jmp' commands with 'nop' commands in a depth-first search.
    Otherwise commands will loop infinitely.

    Return: the next command to execute, counter
    '''
    orig_inp = inp[:]
    next_i = 0
    while next_i != (len(orig_inp)):
        for i in range(len(orig_inp)):
            instru = orig_inp[i].split(" ")[0]
            num = int(orig_inp[i].split(" ")[1])
            new_inp = orig_inp[:]
            if instru == "jmp":
                new_inp[i] = ' '.join(['nop', str(num)])
                print("replaced", orig_inp[i])
            elif instru == "nop":
                new_inp[i] = ' '.join(['jmp', str(num)])
                print("replaced", orig_inp[i])
            next_i, counter = run_all(new_inp)
            if next_i == len(inp):
                break
    return counter

# Task Calls
## Task 1
run_all(inp)
## Task 2
run_all_caveat(inp)
