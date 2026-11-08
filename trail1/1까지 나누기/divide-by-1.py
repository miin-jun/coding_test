N = int(input())

num = 1
while True:
    N = N // num

    if N <=1:

        break
    else:
        num += 1
        continue
print(num)