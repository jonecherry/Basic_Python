#coding=utf-8
def jisuan(s):
    length = len(s)
    if length ==0:
        print 'No!'
        return
    q = 0
    h = length - 1
    while q <= h:
        if not s[q] == s[h]:
            print 'No!'
            return
        q = q+1
        h = h-1
    print 'Yes'
    return

while 1:
    zifucuan = raw_input()
    jisuan(zifucuan)