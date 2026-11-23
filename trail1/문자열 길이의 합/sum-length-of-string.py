N = int(input())
arr = []
cnt = 0
string_len = 0
for _ in range(N):
    string = input()
    string_len +=len(string)
    if "a" in string[0]:
        cnt += 1
print(string_len, cnt)