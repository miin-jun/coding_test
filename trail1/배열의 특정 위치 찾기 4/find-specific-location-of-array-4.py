arr = list(map(int,input().split()))

cnt = 0
even_num = []
for i in range(10):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        even_num.append(arr[i])
        cnt += 1

print(cnt, sum(even_num))