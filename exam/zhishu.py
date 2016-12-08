#coding=utf-8
import copy
import math
sum = int(raw_input())

shus = range(2,1000)
hh = copy.deepcopy(shus)
for shu in shus:
    pingfanggen = int(math.sqrt(shu))
    for pi in range(2,pingfanggen+1):
        if shu%pi==0:
            if shu in hh:
                hh.remove(shu)
            continue

zhishus = [1]
for z in hh:
    zhishus.append(z)

# print zhishus

duishu = 0
length = len(zhishus)
for i in range(length):
    for j in range(length):
        if j < i:
            continue
        if zhishus[i]+zhishus[j]== sum:
            print zhishus[i],zhishus[j]
            duishu = duishu +1
print duishu