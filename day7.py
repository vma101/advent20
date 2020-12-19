'''
Advent of Code
Day 7: Handy Haversacks
https://adventofcode.com/2020/day/7

'''
import re as re

with open("7.txt", "r") as rows:
    inp = [row.rstrip("\n") for row in rows]

# Task 1
def bag_inside(inp, valid = ["shiny gold bag"]):
    '''
    Given a list of rules of < color bag > contains < # other color bags >
    Compute all bags that can contain the first bag provided in < valid > 

    Return: number of possible bags
    '''
    touched = 0
    done = 0
    count = 0
    while done == 0:
        touched = 0
        for i in range(len(inp)):
            rule = inp[i].split('contain')
            color = rule[0].split(' bags')[0]
            for bag in valid:
                if bool(re.search(bag, rule[1])) and bool(color not in valid):
                    touched += 1
                    valid += [color]
                    print(i, touched)
            if i == (len(inp) - 1) and touched == 0:
                done = 1
    return valid, len(set(valid)) - 1

print(bag_inside(inp))

# Task 2
def split_rule(row):
    '''
    Given one rule of < color bag > contains < # other color bags >

    Return 'color' key and '# color' values
    '''
    rule = row.split('contain')
    color = rule[0].split(' bags')[0]
    inside_bags = re.findall("([0-9]+) ([a-z ]+?) bag", rule[1])
    return color, inside_bags

def rule_dict(inp):
    '''
    Given a list of rules of < color bag > contains < # other color bags >
    
    Return: dictionary of 'color' keys and inside bags '# color' values
    '''
    rules = {}
    for row in inp:
        color, inside_bags = split_rule(row)
        rules[color] = inside_bags
    return rules

def bag_outside(rules, color):
    '''
    Given a list of rules of < color bag > contains < # other color bags >
    Compute all bags that can be contained the first bag provided in < valid > 

    Return: number of possible bags
    '''
    count = 0
    inside_bags = rules[color]
    for entry in inside_bags:
        num = int(entry[0])
        color = entry[1]
        print(num, color)
        count += num
        count += num * bag_outside(rules, color)
    return count

rules = rule_dict(inp)
print(bag_outside(rules, 'shiny gold bag'))