arr = list(map(int,input().split()))

even_arr = []
three_arr = []
for i in range(1,10):
    if i % 2 == 1:
        even_arr.append(arr[i])
    if i % 3 ==2:
        three_arr.append(arr[i])

three_avg = (sum(three_arr)/len(three_arr))
print(sum(even_arr), round(three_avg,1))