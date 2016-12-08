# -*- coding:utf-8 -*-


class Flip:
    def flipChess(self, A, f):
        hang = len(A)
        lie = len(A[0])
        for f1 in f:
            x = f1[0]-1
            y = f1[1]-1
            weizhi = []
            if x-1>=0:
                weizhi.append([x-1,y])
            if y-1>=0:
                weizhi.append([x,y-1])
            if x+1<= lie-1:
                weizhi.append([x+1,y])
            if y+1<= hang-1:
                weizhi.append([x,y+1])
            for wei in weizhi:
                xx = wei[0]
                yy = wei[1]
                if A[xx][yy]==0:
                    A[xx][yy]=1
                else:
                    A[xx][yy]=0
        return A
