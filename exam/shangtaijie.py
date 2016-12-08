#coding=utf-8
n = int(raw_input())
for i in range(n):
    def f(shu):
        if shu==2:
            return 1
        if shu ==3:
            return 2
        return f(shu-1)+f(shu-2)

    m = int(raw_input())
    temp = f(m)
    print temp

