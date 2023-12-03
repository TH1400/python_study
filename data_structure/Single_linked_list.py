N = 100001

e = [0] * N
ne = [0] * N
idx = 0
head = -1 # head指向头结点，初始head=-1，即为空集


def insert(x, y):
    global idx
    e[idx] = y
    ne[idx] = ne[x]
    ne[x] = idx
    idx += 1


def delete(x):
    ne[x] = ne[ne[x]]


def to_head(x): # head指向新节点，新节点指向原来的head节点
    global idx, head
    e[idx] = x
    ne[idx] = head
    head = idx
    idx += 1


n = int(input())
for i in range(n):
    op = list(input().split())
    if op[0] == "H":
        to_head(int(op[1]))
    elif op[0] == "I":
        insert(int(op[1]) - 1 , int(op[2]))
    else:
        if op[1] == '0':
            head = ne[head]
        else:
            delete(int(op[1]) - 1)
j = head
while j != -1:
    print(e[j], end=' ')
    j = ne[j]