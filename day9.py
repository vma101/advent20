'''
Advent of Code
Day 9: Handheld Halted
https://adventofcode.com/2020/day/9

'''

day = 9
import re as re

def open_inp(day):
    with open("{}.txt".format(day), "r") as rows:
        inp = [int(row.rstrip("\n")) for row in rows]
    return inp

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        inp = [int(row.rstrip("\n")) for row in rows]
    return inp

### TOGGLE
inp = open_inp(day)
# inp = open_sample(day)

# Task 1
def first_invalid(inp, maxsize = 25):
    '''
    Given a list of numbers, find the first number that is not a combination
    of two previous numbers within the last < maxsize > entries.

    Return: int
    '''
    # initialize the queue
    q = inp[0:maxsize]
    target = maxsize
    num1 = 0
    num2 = num1 + 1
    while num1 < maxsize - 1:
        num1 = 0
        num2 = num1 + 1
        print("before", num1, num2, target)
        while (q[num1] + q[num2] != inp[target]):
            print("iterating", num1, num2, target, q[num1]+q[num2], inp[target])
            if num2 == maxsize - 1:
                num1 += 1
                num2 = num1 + 1
            else:
                num2 += 1
            if num2 == maxsize:
                print("abort", inp[target])
                return target
                break
        q.pop(0)
        q.append(inp[target])        
        target += 1
    return target

def task2(inp, target):
    '''
    Given a list of numbers and a target number, find a contiguous list of terms
    within the list that sum to the target.

    Return: smallest + largest term in the contiguous list
    '''
    sum_target = inp[target]
    num1 = 0
    num2 = num1 + 2
    contig_list = inp[num1:num2]
    while sum(contig_list) != sum_target:
        if num2 == len(inp):
            num1 += 1
            num2 = num1 + 2
        else:
            num2 += 1
        contig_list = inp[num1:num2]
        # if sum(contig_list) == sum_target:
        #     print("done", num1, num2, contig_list[0] + contig_list[-1], sum_target)
        #     break
        # print(num1, num2, inp[num1] + inp[num2 - 1], sum_target)
        print(num1, num2, min(contig_list) + max(contig_list), sum_target)
    return


# Task Calls
first_invalid(inp, 5)
task2(inp, first_invalid(inp))
    

