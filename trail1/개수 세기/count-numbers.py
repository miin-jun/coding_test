N, M = map(int,input().split())

list_N = list(map(int,input().split()))

if M in list_N:
    print(list_N.count(M))