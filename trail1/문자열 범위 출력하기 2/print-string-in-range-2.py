str= input()
cnt = int(input())
str_len = len(str)

if cnt > str_len:
    print(str[::-1])
else:
    i=str_len
    for _ in range(cnt):
        print(str[i-1], end="")
        i -= 1