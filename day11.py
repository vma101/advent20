'''
Advent of Code
Day 11: Seating System
https://adventofcode.com/2020/day/11

'''

day = 11
import re as re
import numpy as np

def open_inp(day):
    with open("{}.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        inp_lists = np.array([list(row) for row in inp])
    return inp_lists

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        inp_lists = np.array([list(row) for row in inp])
    return inp_lists

### TOGGLE
inp = open_inp(day)
# inp = open_sample(day)

adj = np.array([
    # same row
    (0, -1), (0, 1),
    # row above
    (1, -1), (1, 0), (1, 1),
    # row below
    (-1, -1), (-1, 0), (-1, 1)
]) 

def oneSeat(inp, seat_row, seat_col):
    '''
    Given a location on the grid and the grid itself.
    compute the new value of the location.

    Return: new location value, change (1 or 0)
    '''
    # output variables
    seat_val = inp[seat_row, seat_col]
    change = 0

    # counting variables and arrays
    adj_count = 0
    mul = np.ones(adj.shape[0])
    check = np.ones(adj.shape[0])

    # initialize empty variables to increment adjacent seats    
    adj_seat = (0, 0)
    seat = (0, 0)

    # setting limits for edge cases
    col_lim = inp.shape[1] - 1
    row_lim = inp.shape[0] - 1

    # floor space
    if seat_val == '.':
        return seat_val, change
    
    # empty seat, all nearest 8 valid adj must all be empty to become occupied
    elif seat_val == 'L':
        while sum(check) > 0:
            for seat_id in range(len(adj)):
                # check to see if that adj direction needs to be checked
                if check[seat_id] == 0:
                    continue
                else:
                    seat = adj[seat_id]*check[seat_id]*mul[seat_id]
                    adj_seat = (int(seat_row + seat[0]), int(seat_col + seat[1]))
                
                    # check to see that seat is valid
                    if 0 <= adj_seat[0] <= row_lim and 0 <= adj_seat[1] <= col_lim:
                        if inp[adj_seat] == "#":
                            return seat_val, change
                        # if the seat checked is empty, set that seat binary repr to 0
                        elif inp[adj_seat] == "L":
                            check[seat_id] = 0
                            adj_count += 1
                    # if the seat checked is an edge seat, set that seat binary repr to 0
                    else:
                        check[seat_id] = 0
                        adj_count += 1

            # when all binary repr are 0, could be because seats are empty, or edge seat reached
            if adj_count == 8:
                change += 1
                return '#', change
            # check if any more directions are still unaccounted for
            if sum(check) > 0:
                mul += 1
            else:
                return seat_val, change
            # print("checked", seat, mul, check)

    # occupied seat, 5 / 8 adj seats must be occupied to become empty
    elif seat_val == "#":
        while sum(check) > 0:
            for seat_id in range(len(adj)):
                # check to see if that adj direction needs to be checked
                if check[seat_id] == 0:
                    continue
                else:
                    seat = adj[seat_id]*check[seat_id]*mul[seat_id]
                    adj_seat = (int(seat_row + seat[0]), int(seat_col + seat[1]))

                    # check that the seat is valid
                    if 0 <= adj_seat[0] <= row_lim and 0 <= adj_seat[1] <= col_lim:
                        # if adj seat is occupied, that direction no longer needs to be checked
                        if inp[adj_seat] == "#":
                            check[seat_id] = 0
                            adj_count += 1
                            # print(adj_occ, "after traversing seat", adj)
                        elif inp[adj_seat] == "L":
                            check[seat_id] = 0

                    # if the seat checked is an edge seat, set that seat binary repr to 0
                    else:
                        check[seat_id] = 0
        
            # check if 5/8 or more adj seats are occupied
            if adj_count >= 5:
                change += 1
                return 'L', change
            # check if any more directions are still unaccounted for
            if sum(check) > 0:
                mul += 1
            else:
                return seat_val, change
            # print("checked", seat, mul, check)
    
    return seat_val, change    

def oneRound(inp):
    '''
    Given a grid, compute new grid after 1 round

    Return: new grid (array), number of value changes
    '''
    change_count = 0
    inp_new = np.empty(inp.shape, dtype = str)
    for row in range(len(inp)):
        for col in range(len(inp[row])):
            seat_val, change = oneSeat(inp, row, col)
            change_count += change
            inp_new[row, col] = seat_val
    return inp_new, change_count
         
def task1(inp):
    change_count = 1
    inp_new = inp
    while change_count > 0:
        inp_new, change_count = oneRound(inp_new)
        # print("going!")
    
    def occ(x):
        if x == "#":
            return 1
        else:
            return 0

    vOcc = np.vectorize(occ)

    return sum(sum(vOcc(inp_new)))

def task2(inp):
    change_count = 1
    inp_new = inp
    while change_count > 0:
        inp_new, change_count = oneRound(inp_new)
        # print("going!")
    
    def occ(x):
        if x == "#":
            return 1
        else:
            return 0

    vOcc = np.vectorize(occ)

    return sum(sum(vOcc(inp_new)))

# Task Calls
print(task1(inp))
print(task2(inp))