a = input()
b = input()
c = input()

a_len = len(a)
b_len = len(b)
c_len = len(c)

len_max = max(a_len, b_len, c_len)
len_min = min(a_len, b_len, c_len)

print(len_max - len_min)