'''
Advent of Code
Day 4: Passport Processing
https://adventofcode.com/2020/day/4

'''

import re as re

with open("4.txt", "r") as rows:
    inp = [row.rstrip("\n") for row in rows]

def parse_passport(inp, part2 = False):
    valid_count = 0
    row_val = 0
    passport_count = 0
    for i in range(len(inp)):
        if inp[i] == "" or i == (len(inp)):
            if part2 = True:
                if task1(inp[row_val:i]) == 1:
                    print(row_val, i)
                    valid_count += task2(inp[row_val:i])
            else:
                valid_count += task1(rows)
            row_val = i + 1
            passport_count += 1
    return valid_count, passport_count

def task1(rows):
    '''
    Given a single passport, check if they are valid.
    Validity is determined by completeness of the given fields.

    Return: Validity of passport (1 / 0)
    '''
    valid = 0
    passport = " ".join(rows)
    if (passport.find("byr:") != -1) and (passport.find("iyr:") != -1):
        if (passport.find("eyr:") != -1) and (passport.find("hgt:") != -1):
            if (passport.find("hcl:") != -1) and (passport.find("ecl:") != -1):
                if (passport.find("pid:") != -1):
                    valid = 1
    return valid

def task2(rows):
    '''
    Given a single passport, check if they are valid.
    Validity is determined by content of the fields.

    Return: Validity of passport (1 / 0)
    '''
    valid = 0
    passport = " ".join(rows) + " "
    byr = passport[passport.find("byr:")+4:passport.find("byr:") + 8]
    iyr = passport[passport.find("iyr:")+4:passport.find("iyr:") + 8]
    eyr = passport[passport.find("eyr:")+4:passport.find("eyr:") + 8]
    hgt = passport[passport.find("hgt:")+4:passport.find("hgt:") + 9]
    hcl = passport[passport.find("hcl:")+4:passport.find("hcl:") + 11]
    ecl = passport[passport.find("ecl:")+4:passport.find("ecl:") + 7]
    pid = passport[passport.find("pid:")+4:passport.find("pid:") + 13]
    # print(byr, iyr, eyr, hgt, hcl, ecl, pid)

    if bool(re.match("19[2-9][0-9]|200[0-2]", byr)):
        if bool(re.match("201[0-9]|2020", iyr)):
            if bool(re.match("202[0-9]|2030", eyr)):
                if bool(re.match("1[5-8][0-9]cm|19[0-3]cm", hgt)) or bool(re.match("59in|6[0-9]in|7[0-6]in", hgt)):
                    if bool(re.match("^#[0-9a-f]{6}", hcl)):
                        if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
                            if bool(re.match("[0-9]{9}", pid)):
                                valid = 1
    print("{} is {}".format(passport, valid))
    return valid

print(parse_passport(inp))
print(parse_passport(inp, part2 = True))
