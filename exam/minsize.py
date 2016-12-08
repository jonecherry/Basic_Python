#!/usr/bin/env python
# coding=utf-8
# Python使用的是2.7，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
hangshu = 0
arr=[]
lujin = []

start = 0
end = 0
startend = ''


def jisuan(start,end,arr):
    totalsize = 0
    starts = []
    for i in range(len(arr)):
        starts.append(arr[i][0])
    print start
    while 1:
        for i in range(len(arr)):
            if arr[i][0]== start:
                print start,end,totalsize
                totalsize = totalsize + arr[i][2]

                start = arr[i][1]
                if start == end :

                    print totalsize
                    break
                if start not in starts:
                    print False
                    break
                    # break
while 1:
    line = raw_input()
    if line != "":

        if hangshu ==0:
            startend = line
            start = startend.split()[0]
            start = int(start)
            end = startend.split()[1]
            end = int(end)

        else:
            newarrline = []
            line = line.split()
            qian = int(line[0])
            hou = int(line[1])
            size = int(line[2])
            newarrline = [qian,hou,size]
            arr.append(newarrline)



        hangshu = hangshu +1


    else:

        print arr,start,end
        jisuan(start,end,arr)
        break