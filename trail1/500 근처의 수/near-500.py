
arr = list(map(int,input().split()))

arr = sorted(arr)
for num in arr:
    if num >= 500:
        arr_500_index = arr.index(num)
        break

under_500 = arr[:arr_500_index]
over_500 = arr[arr_500_index :]

print(max(under_500),min(over_500))
