N = int(input())
strings = []
for _ in range(N):
    string = input()
    strings.append(string)
first_str = input()

cnt = 0
str_cnt = 0
for str in strings:
    if first_str == str[0]:
        cnt +=1
        str_cnt +=len(str)

print(cnt, f"{str_cnt/cnt:.2f}")