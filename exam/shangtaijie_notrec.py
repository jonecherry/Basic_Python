#coding=utf-8

n = int(raw_input())
index = 3
a1 = 1
a2 = 2
if n ==1:
    print 1
elif n==2:
    print 2
else:
    while index <=n:
        a = a1 + a2
        a1 = a2
        a2 = a
        index  = index + 1
    print a