arr = list(map(int,input().split()))

odd = []
even = []
for i in range(len(arr)):
    if i % 2 == 0 or i==0:
        odd.append(arr[i])
    elif i%2==1:
        even.append(arr[i])
odd_sum = sum(odd)
even_sum = sum(even)

print(abs(odd_sum - even_sum))
