num = []
cnt = 0
while True:
    try:
        N = int(input())
        num.append(N)
        if not (N >=1 and N <=100):
            break
    except EOFError:
        break

for i in range(len(num)):
    if num[i] % 2 !=0:
        continue
    else:
        print(num[i] // 2)
        cnt += 1
        if cnt == 3:
            break
        