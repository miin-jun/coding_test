N = int(input())

if N > 2:
    for i in range(2, N):
        if N % i == 0:
            print("C")
            break
        elif i == (N-1):
            print("N")
else:
    print("N")
