N = 100010
trie = [[0]*26 for _ in range(N)]
count = [0] * N
idx = 1


def insert(x):
    p = 0
    global idx
    for i in range(len(x)):
        u = ord(x[i]) - ord('a')
        if not trie[p][u]:
            trie[p][u] = idx
            idx += 1
        p = trie[p][u]
    count[p] += 1


def query(x):
    p = 0
    for i in range(len(x)):
        u = ord(x[i]) - ord('a')
        if not trie[p][u]:
            return 0
        p = trie[p][u]
    return count[p]


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        op = input().split()
        if op[0] == 'I':
            insert(op[1])
        else:
            print(query(op[1]))