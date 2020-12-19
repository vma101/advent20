'''
Advent of Code
Day 5: Binary Boarding
https://adventofcode.com/2020/day/5

'''

with open("5.txt", "r") as rows:
    inp = [row.rstrip("\n") for row in rows]

def parse_letter(letter, range_list):
    '''
    Given a single digit
    - compute binary range depending on the digit set
    - row (B, F)
    - col (L, R)
    
    Return: low and high of range, as integers
    '''
    end_low = range_list[0]
    end_high = range_list[1]
    if letter == "B" or letter == "R":
        end_low = end_low + (range_list[1] - range_list[0] + 1)//2
    elif letter == "F" or letter == "L":
        end_high = end_high - (range_list[1] + 1 - range_list[0])//2
    # print(end_low, end_high)
    return end_low, end_high

def parse_passes(inp):
    '''
    Given a list of strings made up of only B, R, F, L
    - compute corresponding row (B, F) and col (L, R) through binary search
    - where row can range from 0, 127
    - where col can range from 0, 7
    Compute corresponding IDs defined as <row * 8 + col>
    
    Return: the highest ID
    '''
    highest = 0
    for seatpass in inp:
        row_low = 0
        row_high = 127
        col_low = 0
        col_high = 7
        for i in range(len(seatpass)):
            if i >= 0 and i <= 6:
                # print(seatpass[i])
                row_low, row_high = parse_letter(seatpass[i], [row_low, row_high])
            elif i >= 7:
                col_low, col_high = parse_letter(seatpass[i], [col_low, col_high])
            if col_low == col_high and row_low == row_high:
                seat = row_low * 8 + col_low
                # print(seat)
                if seat >= highest:
                    highest = seat
                    # print("new highest seat id: {}".format(highest))
            else:
                print(row_low, row_high, col_low, col_high)
    return highest                

def missing_seat(inp):
    '''
    Given a list of strings made up of only B, R, F, L
    Compute all IDs (according to earlier definition)
    
    Return: gaps in the range of IDs
    '''
    missing = 0
    seats = []
    for seatpass in inp:
        row_low = 0
        row_high = 127
        col_low = 0
        col_high = 7
        for i in range(len(seatpass)):
            if i >= 0 and i <= 6:
                # print(seatpass[i])
                row_low, row_high = parse_letter(seatpass[i], [row_low, row_high])
            elif i >= 7:
                col_low, col_high = parse_letter(seatpass[i], [col_low, col_high])
            if col_low == col_high and row_low == row_high:
                seat = row_low * 8 + col_low
                print(seat)
                seats.append(seat)

    seats = set(seats)
    index = set(range(875))
    print(min(seats))
    print(index - seats)
    return index = seats  

# Task Calls
## Task 1
print(parse_passes(inp))
## Task 2
print(missing_seat(inp))
