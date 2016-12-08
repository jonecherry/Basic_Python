
arr = [1, -2, 3, 10, -4, 7, 2, -5]

sum = 0
cur = 0
for i in range(len(arr)):
    if cur<=0:
        cur = arr[i]
    else:
        cur = cur + arr[i]
    if sum <cur:
        sum = cur

print sum