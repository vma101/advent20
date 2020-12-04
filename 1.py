import pandas as pd
import numpy as np

with open("1.txt", "r") as entries:
    input = [int(entry.rstrip("\n")) for entry in entries]

done = 0

while done == 0:
    for i in range(len(input)):
        for j in range(len(input)):
            if i != j:
                # print(input[i], input[j], input[i] + input[j])
                if (input[i] + input[j]) == 2020:
                    print("final answer: {}, {}, {}".format(input[i], input[j], input[i]*input[j]))
                    done = 1

done = 0

while done == 0:
    for i in range(len(input)):
        for j in range(len(input)):
            for k in range(len(input)):
                if i != j and j != k and i != k:
                    sum_ijk = input[i] + input[j] + input[k]
                    # print(input[i], input[j], input[k], input[i] + input[j] + input[k])
                    if sum_ijk == 2020:
                        print("final answer: {}, {}, {}, {}".format(input[i], input[j], input[k], input[i]*input[j]*input[k]))
                        done = 1