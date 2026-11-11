A = []
B = []
C = []
D = []
for i in range(3):
    symptoms_temperature = list(input().split())
    if int(symptoms_temperature[1]) >= 37:
        if symptoms_temperature[0] == "Y":
            A.append("A")
        else:
            B.append("B")
    elif symptoms_temperature[0] == "Y" and int(symptoms_temperature[1]) < 37:
        C.append("C")
    else:
        D.append("D")

if not len(A) >= 2:
    print(len(A), len(B),len(C),len(D))
else:
    print(len(A), len(B),len(C),len(D),"E")

