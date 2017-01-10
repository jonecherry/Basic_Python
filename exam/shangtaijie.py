#coding=utf-8
def step(n):
    if n ==1:
        return 1
    elif n ==2:
        return 2
    else:
        return step(n-1) + step(n-2)
n = int(raw_input())

print step(n)
