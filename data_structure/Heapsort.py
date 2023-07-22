size = 0
N = 100010
heap = [0] * N


def down(x):
    # t represent the smallest value's axis in the heap
    t = x
    if 2 * x <= size and heap[2 * x] < heap[t]:
        t = 2 * x
    if 2 * x + 1 <= size and heap[2 * x + 1] < heap[t]:
        t = 2 * x + 1
    if t != x:
        heap[t], heap[x] = heap[x], heap[t]
        down(t)


if __name__ == '__main__':
    n, m = map(int, input().split())
    # count the heap from 1 for simple
    heap[1: n + 1] = list(map(int, input().split()))
    size = n
    # sort from the bottom, to confirm the case that the smallest value in the bottom
    for i in range(n, 0, -1):
        down(i)
    while m > 0 :
        # push the root key and delete the root key
        print(heap[1], end=' ')
        heap[1] = heap[size]
        size -= 1
        down(1)
        m -= 1
