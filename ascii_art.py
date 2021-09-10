import sys
import math

l = int(input())
h = int(input())
t = input()


a = ord('A')
ls = []
out =""
for i in t:
    i = i.upper()
    index = ord(i)-a
    if index<0:
        ls.append(l*(ord('Z')-ord('A')+1))
    elif index ==0 :
        ls.append(index)
    else:
        ls.append(l*index)

for i in range(h):
    row = input()
    for each in ls:
        out += str(row[each:each+l])
    out += "\n"
print(out)