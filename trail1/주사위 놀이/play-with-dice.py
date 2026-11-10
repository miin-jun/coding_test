dice = list(map(int,input().split()))

for number in range(1,7):
    cnt = 0
    for dice_number_cnt in dice:
        if number == dice_number_cnt:
            cnt += 1
    print(number,"-",cnt) 