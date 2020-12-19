'''
Advent of Code
Day 14: Docking Data
https://adventofcode.com/2020/day/14

'''
day = 14
import re as re
import numpy as np

def open_input(day):
    with open("{}.txt".format(day), "r") as rows:
        input = [row.rstrip("\n") for row in rows]
        # input_lists = np.array([list(row) for row in input])
    return input

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        input = [row.rstrip("\n") for row in rows]
        # input_lists = np.array([list(row) for row in input])
    return input

### TOGGLE
# inp = open_input(day)
inp = open_sample(day)

def oneMem_task1(mask_val, row, mem_dict):
    # print('called on:', row)
    mask_one = mask_val.replace('X', '1') # both X, 1 = 1; used with & / AND
    mask_zero = mask_val.replace('X', '0') # both X, 0 = 0; used with | / OR

    # parse line
    mem_key = int(re.search("(?<=mem\[)[0-9]+", row).group(0))
    mem_val = int(re.search("(?<=\s\=\s)[0-9]+", row).group(0))

    # mask = X (1), val = 0 --> 0; val = 1 --> 1
    # mask = 0, val = 0 --> 0; val = 1 --> 0
    # mask = 1, val = 0 --> 0; val = 1 --> 1
    val_new = mem_val & int(mask_one, base = 2)
    
    # mask = X (0), val = 0; --> 0; val = 1 --> 1
    # mask = 0, val = 0 --> 0; val = 1 --> 0
    # mask = 1, val = 0 --> 0; val = 1 --> 1
    val_new = val_new | int(mask_zero, base = 2)

    mem_dict[mem_key] = val_new
    # print('added:', int(mask_one, base = 2), mem_key, mem_val, val_new)
    
    return mem_dict

def task1(inp):
    mem_dict = {}
    mask_val = ''

    for row in inp:
        if bool(re.match('^mask', row)):
            mask_val = row.split(' = ')[1]
            # print('new mask:', mask_val)
        elif bool(re.match('^mem', row)):
            mem_dict = oneMem_task1(mask_val, row, mem_dict)
        else:
            print('abort!')

    return sum(mem_dict.values())



def oneMem(mask_val, row, mem_dict):
    # print('called on:', row)
    # mask_one = mask_val.replace('X', '1') # both X, 1 = 1; used with & / AND
    mask_zero = mask_val.replace('X', '0') # both X, 0 = 0; used with | / OR
    mask_digits = []

    for i, digit in enumerate(mask_val):
        if digit == "X":
            new_mask = '0' * i + '1' + '0' * (len(mask_val) - 1 - i)
            mask_digits.append(new_mask)

    # parse line
    mem_key = int(re.search("(?<=mem\[)[0-9]+", row).group(0))
    mem_val = int(re.search("(?<=\s\=\s)[0-9]+", row).group(0))

    # get all possible keys
        # key_zero is the key if all Xs set to 0.
        # mask = X (0), key = 0 --> 0; key = 1 --> 1
        # mask = 0, key = 0 --> 0; key = 1 --> 1
        # mask = 1, key = 0 --> 1; key = 1 --> 1
    key_zero = mem_key | int(mask_zero, base = 2)

    mem_keys = [key_zero]
    for mask in mask_digits:
        # at each floating digit
        # mask = X (1), key = 0 -->  0 > 1; key = 1 --> 1 > 0

        # at all other digits where mask = 0, key = 1, kz = 1
        # new comp - 0: mask = 0, key = 0 --> 0 > 0; key = 1 --> 1 > 1
        # new comp - 0: mask = 1, key = 0 --> 1 > 1; key = 1 --> 1 > 1
        mem_keys += [mem_key ^ int(mask, 2) for mem_key in mem_keys]
        print(mem_keys)
    
    print(mem_keys)
    
    for key in mem_keys:
        mem_dict[key] = mem_val
    # print('added:', int(mask_one, base = 2), mem_key, mem_val, val_new)
    
    return mem_dict

def task2(inp):
    mem_dict = {}
    mask_val = ''

    for row in inp:
        if bool(re.match('^mask', row)):
            mask_val = row.split(' = ')[1]
            # print('new mask:', mask_val)
        elif bool(re.match('^mem', row)):
            mem_dict = oneMem(mask_val, row, mem_dict)
        else:
            print('abort!')

    return sum(mem_dict.values())


# Task Calls
print(task1(inp))
print(task2(inp))