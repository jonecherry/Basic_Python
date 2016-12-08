#coding=utf-8
ar = raw_input()
tiao = []
start = 0
ar = ar.split()
newar = []
for a in ar:
    a = int(a)
    newar.append(a)

for na in newar:
    for i in range(na):

        hh = i + start +1
        hh = hh%5
        if hh ==0:
            hh = 5
        tiao.append(hh)
    if p in tiao:
        print 'Y'
    else:
        print 'N'
    tiao = []
    start = start + na