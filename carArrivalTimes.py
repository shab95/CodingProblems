#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getResult' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arrival
#  2. INTEGER_ARRAY street
#

def getResult(arrival, street):
    # Write your code here
    times = [0 for i in range(len(arrival))]
    timeHM = {}

    for i in range(len(arrival)):
        if arrival[i] not in timeHM:
            timeHM[arrival[i]] = {0: [], 1: []}
        timeHM[arrival[i]][street[i]].append((arrival[i], i))

    currTime = min(arrival)
    currStr = 1
    while currTime <= max(timeHM.keys()):
        otherStr = (currStr + 1) % 2
        if currTime in timeHM:
            car = None
            currStrLen = len(timeHM[currTime][currStr])
            otherStrLen = len(timeHM[currTime][otherStr])
            if currStrLen > 0:
                car = timeHM[currTime][currStr].pop(0)
            elif otherStrLen > 0:
                car = timeHM[currTime][otherStr].pop(0)
                currStr, otherStr = otherStr, currStr

            if currStrLen > 0 or otherStrLen > 0:
                if currTime + 1 not in timeHM:
                    timeHM[currTime + 1] = {currStr: timeHM[currTime]
                                            [currStr], otherStr: timeHM[currTime][otherStr]}
                else:
                    timeHM[currTime + 1][currStr] = timeHM[currTime][currStr] + \
                        timeHM[currTime + 1][currStr]
                    timeHM[currTime + 1][otherStr] = timeHM[currTime][otherStr] + \
                        timeHM[currTime + 1][otherStr]

            if car is not None:
                times[car[1]] = currTime
        currTime += 1

    return times


print(getResult([0, 1, 1, 3, 3], [0, 1, 0, 0, 1]))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arrival_count = int(input().strip())

#     arrival = []

#     for _ in range(arrival_count):
#         arrival_item = int(input().strip())
#         arrival.append(arrival_item)

#     street_count = int(input().strip())

#     street = []

#     for _ in range(street_count):
#         street_item = int(input().strip())
#         street.append(street_item)

#     result = getResult(arrival, street)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
