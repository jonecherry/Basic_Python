#coding=utf-8
import copy
arr = [1,2,3,4]
quanpailie = []

def f(ar):
    re = []
    for i in range(len(ar)):
        new_ar = ar.remove(ar[i])
        return f(new_ar)




