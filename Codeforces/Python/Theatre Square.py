'''
Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Theatre Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.
'''
import math

inp = input("")


lst = []
num=0

temb = ""

for i in inp:
    num+=1
    temb = temb + i
    if(i == " ") or (num >(len(inp)-1)):
        lst.append(int(temb))
        temb =""




n = lst[0]
m = lst[1]
a = lst[2]
ans = math.ceil(n/a)*math.ceil(m/a)
print(ans)
#print(lst)
