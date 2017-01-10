#coding=utf-8
line = raw_input()
arr = line.split()
arr = map(int,arr)

max = 0
for i in range(len(arr)):
    gao = arr[i]
    kuan = 1

    for j in range(i):
        if arr[i-j-1]>= gao:
            kuan = kuan +1
        else:
            break
    for k in range(len(arr)-i-1):
        if arr[i+k+1]>= gao:
            kuan = kuan + 1
        else:
            break
    print i,gao * kuan
    if gao*kuan> max:
        max = gao*kuan
print max
