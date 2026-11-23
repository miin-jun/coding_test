arr = []
for _ in range(11):
    string = input()
    arr.append(string)

cnt = 0
answer = []
for str in arr[:10]:
    if str[-1] == arr[-1]:
        answer.append(str)
        cnt+=1

if cnt >0 :
    for str in answer:
        print(str)
else:
    print("None")