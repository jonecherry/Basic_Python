#coding=utf-8
arr = [1,1]
n = int(raw_input())
i = 2
while i<31:
    yuansu = arr[i-1] + arr[i-2]
    arr.append(yuansu)
    i = i+1

if n ==1:
    print 1
elif n==2:
    print 1,1
elif n >30:
    print "error"
else:
    newarr = arr[0:n]
    line = ''
    for j in range(len(newarr)):
        line = line +' '+str(newarr[j])
    print line.strip()