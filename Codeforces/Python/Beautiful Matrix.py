'''
You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5).
You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.


'''

w, h = 5, 5
Matrix = [[0 for x in range(w)] for y in range(h)]

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

for i in range(0, 5):
    Line1 = input("")
    Matrix.insert(i, fun(Line1))
"""
Matrix.insert(0, [0,0,0,0,0])
Matrix.insert(1, [0,0,0,0,1])
Matrix.insert(2, [0,0,0,0,0])
Matrix.insert(3, [0,0,0,0,0])
Matrix.insert(4, [0,0,0,0,0])
"""




I = None
J = None
for i in range(0, 5):
    for j in range(0, 5):
        if Matrix[i][j] == 1:
            I = i
            J = j
##print("I ",I)
##print("J ",J)
print(abs(2-I)+abs(2-J))