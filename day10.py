'''
Advent of Code
Day 10: Adapter Array
https://adventofcode.com/2020/day/10

'''
day = 10
import re as re

def open_input(day):
    with open("{}.txt".format(day), "r") as rows:
        input = [int(row.rstrip("\n")) for row in rows]
    return input

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        input = [int(row.rstrip("\n")) for row in rows]
    return input

### TOGGLE
input = open_input(day)
# input = open_sample(day)

def task1(input):
    '''
    Given a list of numbers, sort them in ascending order.
    Count all 1, 3 gap differences between terms.

    Return: # 1 differences * # 3 differences
    '''
    input_sorted = sorted(input)
    ones = 1
    threes = 1
    for i in range(1, len(input_sorted)):
        if input_sorted[i] - input_sorted[i - 1] == 1:
            ones += 1
        elif input_sorted[i] - input_sorted[i - 1   ] == 3:
            threes += 1
    return ones, threes, ones * threes, input_sorted

def task2_recur(input_sub):
    '''
    Given a list of numbers, sorted, return all permutations that can traverse min to max term,
    with gaps between terms of up to 3.
    Key concept: RECURSION

    Return: # methods
    '''
    # set cursor to the end of the loop
    print("called:", input_sub)
    cur = len(input_sub) - 2
    target = len(input_sub) - 1
    # initialize count = 0
    count = 0
    while True:
        assert(cur != target)
        if target == 0:
            count += 1
            break
        elif cur < 0:
            break
        elif (input_sub[target] - input_sub[cur]) <= 3:
            count += task2_recur(input_sub[:cur + 1])
            # print(cur, input_sub, count)
            cur -= 1
        elif (input_sub[target] - input_sub[cur]) > 3:
            break
    print("returning", count)
    return count

def task2(input_sorted):
    '''
    Given a sorted list, return all permutations that can traverse min to max terms,
    with gaps between terms of up to 3.
    Key concept: DYNAMIC PROGRAMMING

    Return: # methods
    '''
    memo = [0] * (max(input_sorted) + 1)
    for num in input_sorted:
        if num <= 3:
            memo[num] = task2_recur(input_sorted[:num + 1])
        else:
            memo[num] = sum(memo[num-3:num])
            print(memo)
    return memo[-1]

# Task Calls
print(task1(input))
input_sorted = sorted(input)
input_sorted.insert(0, 0)
print(task2(input_sorted))