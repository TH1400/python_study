a = [[4, 5, 10], [4, 1, 1], [3, 10, 12]]
b = sorted(a)
c = sorted(a, key=lambda x:(x[2], x[0], x[1]))
print(b)
print(c)