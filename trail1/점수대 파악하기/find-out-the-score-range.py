scores = list(map(int,input().split()))

for tens_digit in range(100,0,-10):
    cnt = 0
    for score in scores:
        if score == 0:
            break
        elif (score // 10) * 10 == tens_digit:
            cnt += 1
    print(tens_digit,"-",cnt)
