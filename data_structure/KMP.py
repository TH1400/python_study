n = int(input())
p = ' ' + input()
m = int(input())
s = input()
ne = [0] * (n + 1)
j = 0
for i in range(2, n+1):
    a, b = p[j], p[i]
    while j and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j

j = 0
for i in range(m):
    while j  and s[i] != p[j+1]:
        j = ne[j]
    if s[i] == p[j+1]:
        j += 1
    if j == n:
        print(i- n+1, end=' ')
        j = ne[j]