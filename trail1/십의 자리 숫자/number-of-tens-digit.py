
arr = list(map(int,input().split()))

for tens_digit in range(1,10):
    cnt = 0
    for number in arr:
        if number == 0:
            break
        elif tens_digit == (number // 10):
            cnt += 1
    print(tens_digit,"-",cnt)