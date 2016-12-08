#coding=utf-8



def lujinshu(shu):


    if shu ==6:
        return 1
    temp = []
    re = 0
    for i in range(length):

        if arr[i][0]== shu :
            temp.append(arr[i][1])
    if len(temp)==0:
        return 0
    else:
        for sh in temp:
            re = re + lujinshu(sh)
        return re

if __name__ == '__main__' :

    arr = [[1,2],[1,3],[2,5],[3,4],[4,6],[5,6]]


    length = len(arr)
    print lujinshu(1)
