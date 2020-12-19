'''
Advent of Code
Day 16: Ticket Translation
https://adventofcode.com/2020/day/16

'''

day = 16
import re as re
import numpy as np

def open_input(day):
    with open("{}.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        # input_lists = np.array([list(row) for row in input])
    return inp

def open_sample(day):
    with open("{}_test.txt".format(day), "r") as rows:
        inp = [row.rstrip("\n") for row in rows]
        # input_lists = np.array([list(row) for row in input])
    return inp

### TOGGLE
inp = open_input(day)
# inp = open_sample(day)

class ticketSystem:
    
    def __init__(self, myTicket, tickets):
        self.rules = {}
        self.myTicket = [int(x) for x in myTicket.split(',')]
        self.tickets = [[int(x) for x in ticket.split(',')] for ticket in tickets]

        self.validCount = 0
        self.invalidSum = 0

        self.validTickets = []
        self.fields = {}
        self.fieldsLoc = {}
    
    def processRule(self, rule):
        field, l1, h1, l2, h2 = re.match(r"([a-z\s]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", rule).groups()
        self.rules[field] = np.array([int(x) for x in [l1, h1, l2, h2]])
    
    def oneValid(self, oneTicket):
        valid = 0
        ticketValid = False
        numValid = False

        for num in oneTicket:
            for l1, h1, l2, h2 in self.rules.values():
                if l1 <= num <= h1 or l2 <= num <= h2:
                    valid += 1
                    numValid = True
                    break
            if not numValid:
                self.invalidSum += num
            numValid = False
    
        if valid == len(oneTicket):
            self.validCount += 1
            ticketValid = True
        return ticketValid
        
    def allValid(self):
        for ticket in [self.myTicket] + self.tickets:
            self.oneValid(ticket)
        return self.validCount, self.invalidSum

    def dropInvalid(self):
        for ticket in [self.myTicket] + self.tickets:
            if self.oneValid(ticket):
                self.validTickets.append(ticket)
        return
    
    def solveTicket(self, oneTicket):
        for field, pos in self.fields.items():
            l1, h1, l2, h2 = self.rules[field]
            
            for i in range(len(oneTicket)):
                num = oneTicket[i]
                if pos[i] == 1 and (num < l1 or h1 < num <l2 or h2 < num):
                    self.fields[field][i] = 0
        return


    def solveFields(self):
        for field in self.rules.keys():
            self.fields[field] = [1]*len(self.myTicket)
        
        # drop invalid tickets
        self.dropInvalid()
        print("valid tickets {} out of {} tickets".format(self.validCount, len(self.tickets) + 1))

        # create the field dictionary
        for ticket in self.validTickets:
            self.solveTicket(ticket)
        self.fields = dict(sorted(self.fields.items(), key = lambda x:x[1]))
        
        # sudoku?
        for field, locList in self.fields.items():
            if sum(locList) == 1:
                self.fieldsLoc[field] = sum(np.array(locList * np.arange(0, len(self.myTicket))))
            else:
                for loc in self.fieldsLoc.values():
                    locList[loc] = 0
                self.fieldsLoc[field] = sum(locList * np.array(locList * np.arange(0, len(self.myTicket))))
        return self.fieldsLoc

    def depFields(self):
        self.solveFields()
        ids = []

        for field in self.fieldsLoc.keys():
            if bool(re.match('^departure', field)):
                ids.append(self.fieldsLoc[field])
        return np.prod([self.myTicket[i] for i in ids])
                           
def processInp(inp):
    '''
    Given input with rules, my ticket ID, other ticket IDs, separated by newline.
    
    Return: ticketSystem class with embedded rules, stored information.
    '''
    ruleList = []
    myTicket = []
    tickets = []
    for row in range(len(inp)):
        if bool(re.match('^your ticket', inp[row])):
            ruleList = inp[:row - 1]
            myTicket = inp[row + 1]
        elif bool(re.match('^nearby tickets', inp[row])):
            tickets = inp[row + 1:]
    ticketSystemClass = ticketSystem(myTicket, tickets)
    for rule in ruleList:
        ticketSystemClass.processRule(rule)
    return ticketSystemClass

def task1(inp):
    '''
    Given input.

    Return: number of invalid tickets, sum of all invalid fields.
    '''
    task1 = processInp(inp)
    validCount, invalidSum = task1.allValid()
    return validCount, invalidSum
    
def task2(inp):
    '''
    Given input.

    Return: product of all departure field values on my ticket.
    '''
    task2 = processInp(inp)
    return task2.depFields()

print(task2(inp))


