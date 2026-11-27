N = input()

i = 1
arr = []
N_list = list(N)
while i < len(N):
    arr.append(N_list[i])
    i += 2
print(*reversed(arr), sep="")

