N = 50001
K = 100001
p = [0 for _ in range(N)]
d = [0 for _ in range(K)]

def find(x):
    if p[x] != x:
        t = find(p[x])
        d[x] += d[p[x]]
        p[x] = t
    return p[x]


if '__main__' == __name__:
    n, m = list(map(int, input().split()))
    res = 0
    for i in range(n):
        p[i] = i
    for _ in range(m):
        op, x, y = map(int, input().split())
        if x > n or y > n:
            res += 1
            continue
        px, py = find(x), find(y)
        if op == 1:
            if px == py and (d[x] - d[y]) % 3:
                res += 1
            else:
                p[px] = py
                d[px] = d[y] - d[x]
        else:
            if px == py and (d[x] - d[y] - 1) % 3:
                res += 1
            else:
                p[px] = py
                d[px] = d[y] + 1 - d[x]
    print(res)