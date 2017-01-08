#coding=utf-8
def xipai(shuzu,n):
    res = []
    for i in range(n):
        res.append(shuzu[2*n-1-i])
        res.append(shuzu[n-1-i])
    res.reverse()
    return res
num_shuzu = int(raw_input())
for i in range(num_shuzu):
    line1 = raw_input().split()
    n = int(line1[0])
    k = int(line1[1])
    line2 = raw_input().strip().split()
    temp = line2
    for j in range(k):
        temp = xipai(temp,n)
    res = ''
    for k in range(2*n):
        res = res +temp[k]+' '

    print res.strip()