N, Q = map(int,input().split())
N_list = list(map(int,input().split()))

for _ in range(Q):
    question = list(map(int,input().split()))
    if question[0] ==1:
        print(N_list[int(question[1])-1])
    elif question[0] ==2:
        if int(question[1]) in N_list:
            print(N_list.index(question[1])+1)
        else:
            print(0)
    else:
        a = question[1]
        b = question[2]
        print(*N_list[a-1:b])




