n = int(input())
number = list(map(int, input().split()))

# Please write your code here.
cnt = 0
min_elem = number[0]
for a in number[1:]:
    if a < min_elem:
        min_elem = a
for b in number:
    if min_elem == b:
        cnt += 1

print(min_elem, cnt)
