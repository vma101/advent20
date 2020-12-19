'''
Advent of Code
Day 3: Toboggan Trajectory
https://adventofcode.com/2020/day/3

'''

with open("3.txt", "r") as rows:
    inp = [row.rstrip("\n") for row in rows]

def tree_check(inp, x, y):
    '''
    Given a grid and an < x, y > position

    Return: if the position is a tree "#" or not "."
    '''
    tree = "no"
    if inp[y][x] == "#":
        tree = "yes"
    return tree

def slope_count(inp, x_incr = 3, y_incr = 1):
    '''
    Given an input grid that repeats itself indefinitely horizontally,
    Traverse it horizonally by < x_incr > steps, vertically by < y_incr >

    Return: number of "#" positions traversed on the way to the bottom
    '''
    trees = 0
    x = x_incr
    y = y_incr
    done = 0
    while done == 0:
        # print(y)
        tree = tree_check(inp, x, y)
        # print("xpos: {}, ypos: {}, tree: {}".format(x, y, tree))
        if tree == "yes":
            trees += 1
        x += x_incr
        y += y_incr
        if x >= len(inp[1]):
            x = x - len(inp[1])
        if y >= len(inp):
            done = 1
    return trees

# Task Calls
def task1(inp):
    return slope_count(inp)

def task2(inp):
    route_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = 1
    for tup in route_list:
        trees = trees * slope_count(inp, tup[0], tup[1])
    return trees

print(task1(inp))
print(task2(inp))

