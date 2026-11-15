n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a_max = max(a)
a.remove(a_max)
a_second = max(a)
print(a_max,a_second)