#coding=utf-8

while 1:
    zifucuan = raw_input().strip()
    if zifucuan !='':
        length = len(zifucuan)
        flag = 0
        i = 0
        j = length-1
        while i<j:
            if j-i==1 and flag==0:
                break
            if zifucuan[i]==zifucuan[j]:
                pass
            else:
                if zifucuan[i+1]==zifucuan[j]:
                    flag = flag +1
                    i = i+1
                elif zifucuan[i]==zifucuan[j-1]:
                    flag = flag +1
                    j = j-1
                else:
                    flag = flag +2
                    break

            i = i+1
            j = j-1
        if flag<=1:
            print "YES"
        else:
            print "NO"
    else:
        break



