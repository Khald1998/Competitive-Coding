'''
You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.

'''
import math

FirstLine = input("")
def fun(x):
    tempList = []
    num = 0

    temb = ""

    for i in x:
        num += 1
        temb = temb + i
        if (i == " ") or (num > (len(x) - 1)):
            tempList.append(int(temb))
            temb = ""
    return tempList

list1 = fun(FirstLine)
M = list1[0]
N = list1[1]

size  = M*N
ans = math.floor(size/2)
print(ans)