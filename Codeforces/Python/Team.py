'''
One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests. Participants are usually offered several problems during programming contests. Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. Otherwise, the friends won't write the problem's solution.

This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.


'''
'''
OLD VIRSION

N = input("")
N = int(N)

Problems = [[0 for x in range(3)] for y in range(N)]
for i in range(0, N):
    for j in range(0, 3):
        Problems[i][j] = input("")


temp=""
for i in range(0, N):
    for j in range(0, 3):

        temp +=str(Problems[i][j])
    temp += "\n"
print(temp)

'''
N = input("")
N = int(N)
wins = 0

for i in range(0, N):
    count=0
    temp = input("")
    L = len(temp)
    for j in range(0, L):
        if temp[j] == "1":
            count+=1

    if count > 1:
        wins+=1
print(wins)


