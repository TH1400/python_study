N = 100010
trie = [[0, 0] for _ in range(N * 31)]
idx = 1


def insert(x):
    p = 0
    global idx
    for k in range(30, -1, -1):
        if not trie[p][x >> k & 1]:
            trie[p][x >> k & 1] = idx
            idx += 1
        p = trie[p][x >> k & 1]



def query(x):
    p = 0
    s = ''
    for k in range(30, -1, -1):
        m = x >> k & 1
        if trie[p][m - 1]:
            s += '1'
            p = trie[p][m - 1]
        else:
            s += '0'
            p = trie[p][m]
    return int(s, 2)


if __name__ == "__main__":
    n = int(input())
    num = input().split()
    res = 0
    for i in range(n):
        insert(int(num[i]))

    for j in range(n):
        res = max(query(int(num[j])), res)
    print(res)
