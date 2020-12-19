'''
Advent of Code
Day 6: Custom Customs
https://adventofcode.com/2020/day/6

'''

with open("6.txt", "r") as rows:
    inp = [row.rstrip("\n") for row in rows]

# Task 1
def parse_groups(inp):
    '''
    Given a list of strings, segment into groups separated by a newline.
    Compute the number of unique letters appearing in each group.

    Return: sum of all groups results
    '''
    questions_sum = 0
    row_val = 0
    for i in range(len(inp)):
        if inp[i] == "":
            questions_sum += parse_group(inp[row_val:i])
            print(i)
            row_val = i + 1
        elif i == (len(inp) - 1):
            questions_sum += parse_group(inp[row_val:i + 1])
    return questions_sum

def parse_group(rows):
    '''
    Given a list of strings (for 1 group)
    Compute the number of unique letters in this group.

    Return: number of unique letters
    '''
    q_string = "".join(rows)
    if len(set(q_string)) > 26:
        print(len(set(q_string)))
    return len(set(q_string))

# Task 2
def parse_groups_yes(inp):
    '''
    Given a list of strings, segment into groups separated by a newline.
    Compute the number of letters that appear in every line for each group.

    Return: sum of all groups results
    '''
    questions_sum = 0
    row_val = 0
    for i in range(len(inp)):
        if inp[i] == "":
            questions_sum += parse_yes(inp[row_val:i])
            print(i)
            row_val = i + 1
        elif i == (len(inp) - 1):
            questions_sum += parse_yes(inp[row_val:i + 1])
    return questions_sum

def parse_yes(rows):
    '''
    Given a list of strings (for 1 group).
    Compute the number of unique letters that appear in every line in this group.

    Return: number of unique letters that appear in each line
    '''
    for i in range(len(rows)):
        if i == 0:
            intersection_set = set(rows[i])
        else:
            set_row = set(rows[i])
            intersection_set = intersection_set.intersection(set_row)
    return len(set(intersection_set))

# Task Calls
print(parse_groups(inp))
print(parse_groups_yes(inp))