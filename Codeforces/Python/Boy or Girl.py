'''
Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.


'''
str = input("")
lis = []
arr = list(str)
arr.sort()
count=0
for i in arr:
    if i not in lis:
        count+=1
        lis.append(i)
num = count%2
if (num == 0):
    ans = "CHAT WITH HER!"
else:
    ans ="IGNORE HIM!"

print(ans)
"""
    s1 = input()  # String.
    s1 = dict.fromkeys(s1)  # Convert it to dictionary to remove duplicates.

    if len(s1) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
"""