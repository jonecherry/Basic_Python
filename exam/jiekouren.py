#!/usr/bin/env python
# coding=utf-8
line = raw_input()
line = line.split()
N = int(line[0])
M = int(line[1])
a = int(line[2])
b = int(line[3])
arr = []
total =0
def path(arr,q,h):
    length = len(arr)
    for j in range(length):
        if arr[j][0] == q and arr[j][1]==b:
            if h ==b:
                total = total +1

                return 'jieshu',0
            else:
                return 'meiji',h



        return 'jieshu',1

for i in range(M):
    jiekou = raw_input()
    jiekou = jiekou.split()
    q = int(jiekou[0])
    h = int(jiekou[1])
    arr.append([q,h])
    qian = a

    tag = ''
    for k in range(len(arr)):
        while tag!='jieshu':
            if arr[k][0]== qian:
                tag,num =  path(arr,q,h)

print arr


