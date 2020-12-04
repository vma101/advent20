import pandas as pd
import numpy as np

with open("2.txt", "r") as entries:
    input = [entry.rstrip("\n") for entry in entries]

valid_count = 0

for i in range(len(input)):
    low = int(input[i][:input[i].find('-')])
    high = int(input[i][input[i].find('-')+1:input[i].find(' ')])
    letter = input[i][input[i].find(' ')+1]
    password = input[i][input[i].find(':')+2:]
    letter_count = sum(map(lambda x : 1 if letter in x else 0, password))
    if letter_count >= low and letter_count <= high:
        valid_count += 1
        print(password)

valid_count = 0
valid = 0

for i in range(len(input)):
    pos1 = int(input[i][:input[i].find('-')]) - 1
    pos2 = int(input[i][input[i].find('-')+1:input[i].find(' ')]) - 1
    letter = input[i][input[i].find(' ')+1]
    password = input[i][input[i].find(':')+2:]
    if password[pos1] == letter and password[pos2] != letter:
        valid = 1
    elif password[pos1] != letter and password[pos2] == letter:
        valid = 1
    if valid == 1:
        valid_count += 1
        valid = 0