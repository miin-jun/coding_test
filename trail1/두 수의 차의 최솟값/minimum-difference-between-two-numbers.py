N = int(input())

arr = list(map(int,input().split()))

abs_list = []
for i in range(N):
    for j in range(i+1,N):
        a = arr[i]- arr[j]
        abs_list.append(abs(a))
abs_list = sorted(abs_list)
print(min(abs_list))

