#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    totalSum = 0
    for cost in bill:
        totalSum += cost

    # Subtract the cost of the item Anna didn't eat
    totalSum -= bill[k]

    # Calculate what Anna's share of the bill should have been
    annaShare = totalSum // 2

    # Check if the charged amount is the same as Anna's share
    if annaShare == b:
        print("Bon Appetit")
    else:
        # Calculate and print the amount Brian needs to refund Anna
        print(b - annaShare)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
