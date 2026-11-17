N = int(input())


for i in range(N):
    number = i + 1
    for j in range(N):
        print(number, end=" ")
        number += N
    print()