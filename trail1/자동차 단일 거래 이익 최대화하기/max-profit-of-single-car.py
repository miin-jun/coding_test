n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

arr = []
for i in range(n):
    for j in range(i+1,n):
        if price[i] < price[j] :
            max_price = int(price[j]) - int(price[i])
            arr.append(max_price)

if len(arr) == 0:
    print(0)
else:
    print(max(arr))
