#coding=utf-8
def topsort(W):
    return W

def dag_sp(W, s, t):
    d = {u:float('inf') for u in W} #
    d[s] = 0
    for u in topsort(W):
        if u == t: break
        for v in W[u]:
            d[v] = min(d[v], d[u] + W[u][v])
            print d[v]
    return d[t]

#邻接表
W={0:{1:2,5:9},1:{2:1,3:2,5:6},2:{3:7},3:{4:2,5:3},4:{5:4},5:{}}
s,t=0,5
print(dag_sp(W,s,t)) #7