sum=0
cnt= 0
while True:
    N = int(input())
    if not (N>=20 and N<30):
        break
    sum += N
    cnt += 1

mean = sum/cnt
print(f"{mean:.2f}")