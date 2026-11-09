N = int(input())

arr = list(map(float,input().split()))

arr_sum = sum(arr)
arr_avg = round(arr_sum / N,1)

if arr_avg >= 4:
    print(arr_avg)
    print("Perfect")
elif arr_avg >= 3:
    print(arr_avg)
    print("Good")
else:
    print(arr_avg)
    print("Poor")

