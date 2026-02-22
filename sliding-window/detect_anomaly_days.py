#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'detectAnomalyDays' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY reservationIds
#  2. INTEGER_ARRAY checkins
#  3. INTEGER_ARRAY checkouts
#
# 0, .... 6
# ....3.....7
# ..2...........13

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# 1 1 1 1 1 1 0 0 0 0 0
# 0 0 0 1 1 1 1 0 0 0 0 0 
#______________________________

# 123, 0, 5 -> discard
# 123, 0, 10 -> this value



# 1 1 1 2 2 2 1 0
# 1 1 1 2 2 2 1 = 10 avg = 10 / 7 = 1.4
# 1.4's 80% compare 0
def detectAnomalyDays(reservationIds, checkins, checkouts):
    # Write your code here
    # [0, 3, 2],  [6, 7, 13]
    # length_res = len(reservationIds)
    # array of reservations for each date [[0,6], [3, 7]]
    # reservation[0] = number of reservations on day 0
    # reservation[i] = number of reservations on day i
    
    # 0,6
    # 
    # for i in range(checkin,checkout)
    #    reservation[i] +=1
    reservations_per_day = []
    result = []
    # [5, 7, 8, 8, 0, 7, 8]
    for i in range(len(checkins)):    
        for j in range(checkins[i], checkouts[i]):
            reservations_per_day[i] += 1

    # We want to detect all the dates that have a number of active reservations less than 80% of the previous 7 days average.
    
    for i in reservations_per_day:
        if i < 7:
            continue
            
        average_last_7 = sum(reservations_per_day[i-7],reservations_per_day[i])/7
        
        eighty_percent= average_last_7 * 0.8
        
        if reservations_per_day[i] < eighty_percent:
            result.append(i)
            
    return result
    
    # sum reservations_per_day[i - 7].. [1 - 1]/ 7
    # 40 * 0.8 = 32
    # reservations_per_day[i]
    
    # add i to the result list
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    reservationIds_count = int(input().strip())

    reservationIds = []

    for _ in range(reservationIds_count):
        reservationIds_item = int(input().strip())
        reservationIds.append(reservationIds_item)

    checkins_count = int(input().strip())

    checkins = []

    for _ in range(checkins_count):
        checkins_item = int(input().strip())
        checkins.append(checkins_item)

    checkouts_count = int(input().strip())

    checkouts = []

    for _ in range(checkouts_count):
        checkouts_item = int(input().strip())
        checkouts.append(checkouts_item)

    result = detectAnomalyDays(reservationIds, checkins, checkouts)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()