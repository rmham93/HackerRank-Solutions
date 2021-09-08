 #!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    #we will use dictionary
    dic = dict() 
    #traversing array will cost O(n)
    for i in range(len(arr)):
        if arr[i] in dic.keys():
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
 
    # find the max frequency
    max_count = 0
    res = -1
    #We traverse dictionary to find most frequent item
    for i in dic:
        if (max_count < dic[i]):
            res = i
            max_count = dic[i]
        elif  max_count == dic[i]:
            #if two items are most freq. then take min id
            if res >i:
                res = i
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
