N = int(input())

number = list(map(int,input().split()))
even_number = []
for i in range(len(number)):
    if number[i] % 2 == 0 or number[i] ==0:
        even_number.append(number[i])

print(*even_number[::-1])
