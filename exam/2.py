#coding=utf-8
arr = [1024,512,256,128,64,32,16,8,4,2]
N = int(raw_input())
res = 0
while res!=1:
    if N in arr:
        print 'true'
        break
    if N%2==1:
        print 'false'
        break
    else:
        N = N/2


