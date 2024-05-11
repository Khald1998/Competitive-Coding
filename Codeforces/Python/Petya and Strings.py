"""
Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

"""
Line1 = input("")
Line1 = Line1.lower()
Line2 = input("")
Line2 = Line2.lower()
A = ''
B = ''
if Line1 == Line2:
    ans = 0
else:
    L = len(Line1)
    for i in range(0, L):

        if Line1[i] < Line2[i] and Line1[i] != Line2[i]:
            ans = -1
            break
        elif Line1[i] > Line2[i] and Line1[i] != Line2[i]:
            ans = 1
            break



print(ans)