arr = list(map(int,input().split()))

cnt = 0
for i in range(10):
    if arr[i] !=0:
        cnt += 1
    if arr[i] ==0:
        break

arr_sum = sum(arr[:cnt])
avg = round(arr_sum /cnt,1)
print(arr_sum, avg)