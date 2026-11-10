arr = list(map(int,input().split()))

arr_sum =[]
for i in range(3,len(arr)):
    if arr[i] == 0:
        for j in range(i-1,i-4,-1):
            arr_sum.append(arr[j])
        break

print(sum(arr_sum))
