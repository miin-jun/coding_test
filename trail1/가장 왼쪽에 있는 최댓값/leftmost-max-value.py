n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

arr = []
while True:
    if len(a) >=1:
        a_max = max(a)
        a_max_index = a.index(a_max)
        arr.append(a_max_index +1)
        a = a[:a_max_index]
        if len(a) ==0:
            break
print(*arr)