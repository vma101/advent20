'''
Advent of Code
Day 18: Operation Order
https://adventofcode.com/2020/day/18

'''
day = 18
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

def oneSum(expr):
    print('called on:', expr)
    exprSum = 0
    exprSub = ''
    exprTerms = expr.strip().split(' ')
    
    brCount = 0
    cur = len(expr) - 1
    if expr[-1] == ')':
        print("branch 1")
        brCount += 1
        while brCount > 0:
            cur -= 1
            if expr[cur] == '(':
                brCount -= 1
            elif expr[cur] == ')':
                brCount += 1
        exprBr = expr[cur + 1: -1]
        newExpr = '{}{}'.format(expr[:cur], oneSum(exprBr))
        exprSum += oneSum(newExpr)

    elif len(exprTerms) > 3:
        print("branch 2")
        exprSub = ' '.join(exprTerms[:-2])
        newExpr = '{} {}'.format(oneSum(exprSub), ' '.join(exprTerms[-2:]))
        exprSum += oneSum(newExpr)

    elif len(exprTerms) == 3:
        print("base")
        exprSum += eval(expr)
    
    elif len(exprTerms) == 1:
        exprSum = exprTerms[0]
    print('returning', exprSub, 'sum', exprSum)
    return int(exprSum)

def task1(inp):
    rowSum = 0
    for row in inp:
        rowSum += oneSum(row)
    return rowSum

# Task 2

class flipMath:
    '''
    Topsy turvy math!
    If operation is *, add. If operation is +, multiply!
    '''

    def __init__(self, term):
        self.val = int(term)
    
    def __add__(self, term2):
        self.val = self.val * term2.val
        return self
    def __mul__(self, term2):
        self.val = self.val + term2.val
        return self

def flipSum(expr):
    print('called on:', expr)
    exprSum = 0
    exprSub = ''
    exprTerms = expr.strip().split(' ')

    # search for parentheses, and 
    parenStart = expr.find('(')
    brCount = 0
    if parenStart != -1:
        cur = parenStart
        brCount += 1
        while brCount > 0:
            cur += 1
            if expr[cur] == ')':
                brCount -= 1
            elif expr[cur] == '(':
                brCount += 1
        exprSub = expr[parenStart + 1: cur]
        if cur == len(expr) - 1:
            newExpr = expr[:parenStart] + str(flipSum(exprSub))
        else:
            newExpr = expr[:parenStart] + str(flipSum(exprSub)) + expr[cur + 1:]
        exprSum = flipSum(newExpr)

    else:
        newExpr = expr.replace("+", "-").replace("*", "+").replace("-", "*")
        newExpr = re.sub(r"(\d+)", flipFn, newExpr)
        exprSum += eval(newExpr, {'flipMath': flipMath}).val   
    
    print('returning', exprSub, 'sum', exprSum)
    return exprSum

def flipFn(match):
    num = int(match.group(0))
    return str(f'flipMath({num})')

def task2(inp):
    rowSum = 0
    for row in inp:
        rowSum += flipSum(row)
    return rowSum

# Task Calls
print(task1(inp))
print(task2(inp))


