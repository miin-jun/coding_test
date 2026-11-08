while True:
    width, length, char = input().split()
    print(int(width) * int(length))
    if char == "C":
        break