def find(a):
    a = int(a)
    while a != p[a]:
        a = p[a]
    return a

if __name__ == "__main__":
    N = 100001
    p = [0] * N
    size = [0] * N
    mn = list(map(int, input().split()))
    for i in range(1, mn[0] + 1):
        p[i] = i
        size[i] = 1

    for i in range(mn[1]):
        op = input().split()
        if op[0] == 'C' :
            if find(op[1]) == find(op[2]): continue
            size[find(op[2])] += size[find(op[1])]
            p[find(op[1])] = find(op[2])
        elif op[0] == "Q1":
            if p[find(op[1])] == p[find(op[2])]:
                print('Yes')
            else:
                print("No")
        else:
            print(size[find(op[1])])