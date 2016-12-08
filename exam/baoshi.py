#!/usr/bin/env python
# coding=utf-8


guolv = ['A','B','C','D','E']



def jisuan():
    max = 0

    for i in range(len(line)):


        if i ==0:
            yuansu = 0
            for t in range(i,len(line)):

                zimu = line[t]

                if zimu not in guolv:

                    yuansu = yuansu +1

                else:
                    break
            for j in range(len(line)):
                zimu1 = line[length-j-1]
                if zimu1 not in guolv:
                    yuansu = yuansu +1

                else:
                    break

            if yuansu > max:

                max = yuansu
        else:
            yuansu = 0
            for t in range(i,len(line)):

                zimu = line[t]
                if zimu not in guolv:
                    yuansu = yuansu +1
                if zimu in guolv:
                    break
            if yuansu > max:
                max = yuansu
    return max

while 1:
    line = raw_input()
    length = len(line)


    if line != "":
        max = jisuan()
        print max
    else:

        break