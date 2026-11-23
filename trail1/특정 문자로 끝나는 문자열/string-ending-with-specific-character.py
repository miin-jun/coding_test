arr = [input() for _ in range(10)]
chr = input()
found = False

for str in arr:
    if chr == str[-1]:
        found = True
        print(str)
    
if found == False:
    print("None")