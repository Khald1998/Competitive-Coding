#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Count the frequency of each type
    type_count = {}
    for bird_type in arr:
        if bird_type in type_count:
            type_count[bird_type] += 1
        else:
            type_count[bird_type] = 1

    # Find the highest count of sightings
    max_count = max(type_count.values())
    
    # Initialize a list to store the most frequently sighted bird types
    most_common = []
    
    # Loop through each bird type and its count
    for bird_type, count in type_count.items():
        # Check if the count is equal to the max_count
        if count == max_count:
            # If so, add the bird type to the list of most common types
            most_common.append(bird_type)

    # Return the smallest type id of the most frequently sighted birds
    return min(most_common)

# Your main code continues from here...

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
