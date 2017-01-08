#coding=utf-8
def chazhao(A, n, val):
    q = 0
    h = n - 1

    while q < h:
        mid = (q + h) / 2
        if val > A[mid]:
            q = mid + 1
        else:
            h = mid
    return q
print chazhao([1,2,3,3,3,4,5,5,6,7,9],10,5)