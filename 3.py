with open("3.txt", "r") as rows:
    input = [row.rstrip("\n") for row in rows]

trees = 0
x = 3
tree = "no"
for y in range(1, len(input)):
    print(y)
    if input[y][x] == '#':
        trees += 1
        tree = 'yes'
    print("xpos: {}, ypos: {}, tree: {}".format(x, y, tree))
    x += 3
    if x >= len(input[y]):
        x = x - len(input[y])
        tree = "no"

def slope_count(input, x_incr = 3, y_incr = 1):
    trees = 0
    x = x_incr
    y = y_incr
    done = 0
    while done == 0:
        # print(y)
        tree = tree_check(input, x, y)
        # print("xpos: {}, ypos: {}, tree: {}".format(x, y, tree))
        if tree == "yes":
            trees += 1
        x += x_incr
        y += y_incr
        if x >= len(input[1]):
            x = x - len(input[1])
        if y >= len(input):
            done = 1
    return trees

def tree_check(input, x, y):
    tree = "no"
    if input[y][x] == "#":
        tree = "yes"
    return tree