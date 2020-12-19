'''
Advent of Code
Day 13: Shuttle Search
https://adventofcode.com/2020/day/13

'''

day = 13
import re as re
import numpy as np

def open_inp(day):
    with open("{}.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        # inp_lists = np.array([list(row) for row in inp])
    return inp

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        # inp_lists = np.array([list(row) for row in inp])
    return inp

### TOGGLE
inp = open_inp(day)
# inp = open_sample(day)

def task1(inp):
    '''
    Given a timestamp, and a list of nums (bus IDs) and strings 'x',
    compute next possible bus and the number of minutes wait from 
    current timestamp

    Return: (array) of next bus times for all numbered buses, soonest bus ID * wait time
    '''
    timestamp = int(inp[0])
    bus_ids = inp[1].split(",")
    bus_ids = np.array([int(x) for x in bus_ids if x != 'x'])
    print(bus_ids)
    
    def next_bus(bus_id):
        rem = timestamp % bus_id
        if rem == 0:
            return rem
        else:
            return bus_id - rem

    bus_times = np.array(list(map(next_bus, bus_ids)))
    return bus_times, min(bus_times)*bus_ids[bus_times.argmin()]

def task2(inp):
    '''
    Given a timestamp, and a list of nums (bus IDs) and strings 'x',
    compute next possible timestamp when all the buses come exactly late for y minutes
    as their indexed positions y

    Return: (array) bus IDs, (array) corresponding wait times.
    Key concept: CHINESE REMAINDER THEOREM
    ** Plug printed bus IDs and corresponding wait times to a CRT calculator.
    '''
    bus_ids = inp[1].split(",")
    bus_waits = np.array([(int(e) - (i)) % int(e) for i, e in enumerate(bus_ids) if e != 'x'])
    bus_ids = np.array([int(x) for x in bus_ids if x != 'x'])

    # N = np.prod(bus_ids)
    # Y = [0] * len(bus_ ids)
    # Z = [0] * len(bus_ids)
    # for bus in range(len(bus_ids)):
    #     Y[bus] = N / bus_ids[bus]
    #     Z[bus] = (1/Y[bus]) % bus_ids[bus]
    
    # prod = np.sum(bus_waits * Y * Z)
    return bus_ids, bus_waits

# Task Calls
print(task1(inp))
print(task2(inp))