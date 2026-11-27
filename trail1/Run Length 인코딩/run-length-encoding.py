A = input()

# Please write your code here.
arr = []
A_list = list(A)

i = 0
while i< len(A_list):
    cnt = 0
    first_string = A_list[i]
    while i < len(A_list):
        
        if first_string == A_list[i]:
            i += 1
            cnt += 1
        else:
            break
    arr.append(first_string)
    arr.append(cnt)


print(len("".join(map(str,arr))))
print(*arr, sep="")