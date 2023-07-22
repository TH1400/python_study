import Scripts.activate_this

N = 100002
size = 0
heap = [0 for _ in range(N)]

def up(x):
    father = x // 2
    if
    while father and heap[father] > heap[x]:
        heap[father], heap[x] = heap[x], heap[father]
        father = father // 2


def down(x):
    pass


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in nums:
        size += 1
        heap[size] = i
        up(size)
    print(' '.join(str(x) for x in heap[1 :m + 1]))