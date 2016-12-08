#encoding=utf-8
import copy
mat = [[1,2,3],[4,5,6],[7,8,9]]
n = 3
n = int(n)
newmat = copy.deepcopy(mat)

for i in range(n):

    for j in range(n):


        x = j
        y = n -1 -i
        print i,j
        print x,y
        newmat[x][y] = mat[i][j]
        print newmat[x][y]
        print newmat
        print '-----'
