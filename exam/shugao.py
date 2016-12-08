#coding=utf-8


def jisuan(arr,q,h):
    hh = [0]
    while 1:
        for j in range(len(arr)):
            if arr[j][1]==h and arr[j][0]==0:
                hh.append(h)
                return hh

        for i in range(len(arr)):
            if arr[i][1] == h:
                hh.append(h)
                h = arr[i][0]

def shuzu(shu):
    for i in range(shu):
        line = raw_input()
        line = line.split()
        temp = [int(line[0]),int(line[1])]
        arr.append(temp)
    return arr

n = int(raw_input())
arr = []

arr = shuzu(n-1)
res =  jisuan(arr,0,n-1)
print res
print len(res)
