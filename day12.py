'''
Advent of Code
Day 12: Rain Risk
https://adventofcode.com/2020/day/12

'''
day = 12
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

dir_dict = {'E': 0, 'S':1, 'W':2, 'N':3}
R_dict = {'E': 'S', 'S':'W', 'W':'N', 'N':'E'}
L_dict = {'E': 'N', 'S':'E', 'W':'S', 'N':'W'}

def oneAction_task1(dir, dist, curr_dir):
    '''
    Given 1 action, compute new direction, and incremental movement.

    Return: new direction, incremental distance (int)
    '''
    dist_add = 0
    if dir in dir_dict.keys():
        return dir, dist
    elif dir == "F":
        return curr_dir, dist
    elif dir == 'L':
        x = dist / 90
        dir = curr_dir
        while x > 0:
            dir = L_dict[dir]
            x -= 1
    elif dir == 'R':
        x = dist / 90
        dir = curr_dir
        while x > 0:
            dir = R_dict[dir]
            x -= 1
    return dir, dist_add
    
def task1(inp):
    '''
    Given a list of instructions, compute Manhattan distance of final position
    from the beginning position (assume 0, 0)

    Return: distance array, Manhattan distance (int)
    '''
    # initialize current state, distance array indexed as E, S, W, N
    curr_dir = 'E'
    dist_arr = [0]* 4

    for row in inp:
        dir = row[0]
        dist = int(row[1:])
        new_dir, new_dist = oneAction_task1(dir, dist, curr_dir)
        dist_arr[dir_dict[new_dir]] += new_dist
        if dir not in dir_dict.keys():
            curr_dir = new_dir
    man_dist = abs(dist_arr[0] - dist_arr[2]) + abs(- dist_arr[1] + dist_arr[3])
    return dist_arr, man_dist


def oneAction(dir, dist, curr_wp):
    '''
    Given current waypoint, new direction and distance incr of a rule

    Return: incremental movement (int), new waypoint
    '''
    move = 0
    wp = curr_wp
    if dir == 'F':
        move = 1
        return move, dist * curr_wp
    elif dir in dir_dict.keys():
        curr_wp[dir_dict[dir]] += dist
        return move, curr_wp
    elif dir == 'R':
        x = dist / 90
        while x > 0:
            # do something
            wp = np.roll(wp, 1)
            x -= 1
    elif dir == 'L':
        x = dist / 90
        while x > 0:
            wp = np.roll(wp, -1)
            x -= 1
    return move, wp


def task2(inp):
    '''
    Given a list of instructions, compute Manhattan distance of final position
    from the beginning position (assume 0, 0)

    Return: distance array, Manhattan distance (int)
    '''
    curr_wp = np.array([10, 0, 0, 1])
    dist_arr = np.zeros(4)

    for row in inp:
        dir = row[0]
        dist = int(row[1:])
        move, wp = oneAction(dir, dist, curr_wp)
        if move == 1:
            dist_arr += wp
        elif move == 0:
            curr_wp = wp

        # making sure that the waypoint is ONLY one of N, S; and ONLY one of E, W
        wp_e = curr_wp[0] - curr_wp[2]
        wp_s = curr_wp[1] - curr_wp[3]
        curr_wp = np.array([max(0, wp_e), max(0, wp_s), max(0, -wp_e), max(0, -wp_s)])
        print(dir, dist, move, curr_wp)
    man_dist = abs(dist_arr[0] - dist_arr[2]) + abs(- dist_arr[1] + dist_arr[3])
    return dist_arr, man_dist

# Task Calls
print(task1(inp))
print(task2(inp))