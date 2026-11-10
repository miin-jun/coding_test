N = int(input())
cnt = 0

pass_or_fail = []
for _ in range(N):
    arr = list(map(int,input().split()))
    arr_sum = sum(arr)
    avg = arr_sum/4
    if avg >= 60:
        pass_or_fail.append("pass")
        cnt += 1
    else:
        pass_or_fail.append("fail")

for j in range(len(pass_or_fail)):
    print(pass_or_fail[j])

print(cnt)