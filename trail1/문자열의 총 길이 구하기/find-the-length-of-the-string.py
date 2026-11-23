string = input().split()

cnt = 0
for i in range(10):
    cnt += len(string[i])

print(cnt)
