# rum-yasuhiro
# 2021.1.31

# import sys
# from collections import deque

l = set()

n = int(input())
for _ in range(n):
    s = input()
    if s[0] == "i":
        l.add(s[7:])
    else:
        if s[5:] in l:
            print("yes")
        else:
            print("no")
