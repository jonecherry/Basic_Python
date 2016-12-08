# -*- coding:utf-8 -*-

class Visit:
    def countPath(self, map, n, m):
        start=(0,0)
        end=(0,0)
        for i in range(n):
            for j in range(m):
                if map[i][j]==1:
                    start=(i,j)
                if map[i][j]==2:
                    end=(i,j)
        if start[0]==end[0] and start[1]==end[1]:
            return 1
        if start[0]<end[0]:
            dir_x=1
        else:
            dir_x=-1
        if start[1]<end[1]:
            dir_y=1
        else:
            dir_y=-1
        dp=[[0 for i in range(m)] for j in range(n)]
        for i in range(start[0],end[0]+dir_x,dir_x):
            for j in range(start[1],end[1]+dir_y,dir_y):
                if map[i][j]==-1:
                    dp[i][j]=0
                elif i==start[0] or j==start[1]:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-dir_x][j]+dp[i][j-dir_y]
        return dp[end[0]][end[1]]