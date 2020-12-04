import re as re

with open("4.txt", "r") as rows:
    input = [row.rstrip("\n") for row in rows]

def parse_passport(input):
    valid_count = 0
    row_val = 0
    passport_count = 0
    for i in range(len(input)):
        if input[i] == "" or i == (len(input)):
            if check_passport(input[row_val:i]) == 1:
                print(row_val, i)
                valid_count += check_passport_depth(input[row_val:i])
            # print("{} is {}"input[row_val:i])
            row_val = i + 1
            print(row_val)
            passport_count += 1
    return valid_count, passport_count

def check_passport(rows):
    valid = 0
    passport = " ".join(rows)
    if (passport.find("byr:") != -1) and (passport.find("iyr:") != -1):
        if (passport.find("eyr:") != -1) and (passport.find("hgt:") != -1):
            if (passport.find("hcl:") != -1) and (passport.find("ecl:") != -1):
                if (passport.find("pid:") != -1):
                    valid = 1
    print("{} is {}".format(passport, valid))
    return valid

def check_passport_depth(rows):
    valid = 0
    passport = " ".join(rows) + " "
    byr = passport[passport.find("byr:")+4:passport.find("byr:") + 8]
    iyr = passport[passport.find("iyr:")+4:passport.find("iyr:") + 8]
    eyr = passport[passport.find("eyr:")+4:passport.find("eyr:") + 8]
    hgt = passport[passport.find("hgt:")+4:passport.find("hgt:") + 9]
    hcl = passport[passport.find("hcl:")+4:passport.find("hcl:") + 11]
    ecl = passport[passport.find("ecl:")+4:passport.find("ecl:") + 7]
    pid = passport[passport.find("pid:")+4:passport.find("pid:") + 13]
    print(byr, iyr, eyr, hgt, hcl, ecl, pid)

    if bool(re.match("[1][9][2-9][0-9]|[2][0][0][0-2]", byr)):
        if bool(re.match("20[1][0-9]|[2][0][2][0]", iyr)):
            if bool(re.match("20[2][0-9]|2030", eyr)):
                if bool(re.search("[1][5-6][0-9]cm|[1][7][0-3]cm", hgt)) or bool(re.search("[5][9]in|[6][0-9]in|[7][0-6]in", hgt)):
                    if bool(re.match("^#[0-9a-f]{6}", hcl)):
                        if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "hzl" or ecl == "oth":
                            if bool(re.match("[0-9]{9}", pid)):
                                valid = 1
    print("{} is {}".format(passport, valid))
    return valid
