#coding=utf-8

line = raw_input()
line = line.split()
global yuansu
global youde,sum,shuzu,index
youde = int(line[len(line)-1])
arr = line[0:len(line)-1]
# 目前剩余的钱
sum = youde
# 将arr 整数化的新数组
arr1 =[]
# 不同方案下的酒店数
res = []
for yuansu in arr:
    arr1.append(int(yuansu))
arr1.sort()
arr1.reverse()
# print arr1


def jisuan(muqiansum):

    global youde,sum,index
    global yuansu
    temparr = []
    temp = muqiansum/arr1[index]
    # if sum%arr1[index]==0:
    #     yuansu = +temp
    #     res.append(yuansu)
    #     return
    #     # return jisuan(sum,yuansu,index+1)

    for i in range(temp+1):
        j = temp-i
        sum = sum- arr1[index]*j

        # print sum,arr1[index],j
        yuansu=yuansu+j
        if sum == 0:
            res.append(yuansu)
            print sum ,yuansu,arr1[index]
            break

        index =index +1
        print sum,yuansu,index
        return jisuan(sum)


# 在具体酒店住的天数\

tag = 0
yuansu = 0
index = 0
jisuan(sum)
res.sort()
print res
# print res[0]
