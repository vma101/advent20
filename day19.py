'''
Advent of Code
Day 19: Monster Messages
https://adventofcode.com/2020/day/19

'''
day = 19
import re as re
import numpy as np

import lark

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
# inp = open_sample(day)
# print(inp)

def parseRules(raw):
    '''
    Parse given raw rules (1 per line) into the following format in preparation
    for creating a parsing tree:
        node<#>: (node<#>).* | (node<#>).*
        - criteria after | is xor in fashion
    
    Return: prepared text
    '''
    rules = ''
    for rule in raw:
        name, ruleAll = re.match('([0-9]+): (.*)', rule).groups()

        # case: secondary rules
        if bool(re.search('\|', ruleAll)):
            cri1, cri2 = re.match('(.*) \| (.*)', ruleAll).groups()
            rule1 = " ".join(['node' + d for d in cri1.split()])
            rule2 = " ".join(['node' + d for d in cri2.split()])
            subRule = ' '.join([rule1, '|', rule2])
        
        # case: string only
        elif bool(re.search("\"", ruleAll)):
            subRule = ruleAll
        
        else:
            subRule = " ".join(['node' + d for d in ruleAll.split()])
        
        # if the name of the rule is 0, set as root of the tree
        if name == '0':
            name = 'start'
        else:
            name = 'node' + name

        # if name in ['node8', 'node11']:
        #     print(name, ruleAll)
        
        rules = rules + (f"{name}: {subRule}\n")
        # print(rules)
    return rules    
    
def task(inp, part2 = False):
    '''
    Given input of rules and messages, count all messages that don't fit within
    the given rules.
    First converts all rules into a parsing tree
    Second feeds messages into parser

    Returns: count of valid messages
    '''
    rulesRaw = inp[:inp.index('')]
    msgs = inp[inp.index('') + 1:]
    valid = 0

    if part2:
        for loc in range(len(rulesRaw)):
            if bool(re.match('^8:', rulesRaw[loc])):
                rulesRaw[loc] = '8: 42 | 42 8'
            elif bool(re.match('^11:', rulesRaw[loc])):
                rulesRaw[loc] = '11: 42 31 | 42 11 31'

    rules = parseRules(rulesRaw)
    parser = lark.Lark(rules)

    for msg in msgs:
        try:
            parser.parse(msg)
            valid += 1
        except:
            pass
    
    return valid

# Task Calls
print(task(inp))
print(task(inp, part2 = True))