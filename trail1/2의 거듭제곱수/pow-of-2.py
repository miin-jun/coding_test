N = int(input())

i = 0
while True:
    N = N // 2
    i += 1
    if N == 1:
        break

print(i)