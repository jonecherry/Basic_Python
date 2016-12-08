#coding=utf-8

num = int(raw_input())
zifucuans = raw_input()
zifucuans = zifucuans.split()
newzifucuans = []

for zifucuan in zifucuans:
    newzifucuans.append(int(zifucuan))

newzifucuans.sort()

zuheshu = 1
for j in range(len(newzifucuans)):
    temp = str(newzifucuans[j])
    guolv = []
    yinzi = 0
    for j in range(len(temp)):
        if temp[j] not in guolv:
            yinzi = yinzi +1
        else:
            yinzi.temp[j]


    zuheshu = zuheshu * yinzi


print zuheshu



