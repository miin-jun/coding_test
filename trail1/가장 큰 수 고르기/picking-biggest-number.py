number = list(map(int,input().split()))

max_elem = number[0]

for a in number[1:]:
    if a > max_elem:
        max_elem = a

print(max_elem)