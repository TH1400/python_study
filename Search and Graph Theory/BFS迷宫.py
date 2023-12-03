from collections import deque

n, m = map(int, input().split())
def dfs():
    # 用a，b来表示移动的步数[-1, 0][1, 0][0, 1][0, -1]
    a, b = [0, 1, 0, -1], [1, 0, -1, 0]
    queue = deque()
    # 初始化队列queue
    queue.append([0,0])
    # 0,0点已被占用
    mark[0][0] = 0

    while queue:
        # 从队尾取出一个数，查看这个点下一步四个方向是否可走
        cur = queue.popleft()
        for i in range(4):
            x = cur[0] + a[i]
            y = cur[1] + b[i]
            # 下一个点在图内且没被走过，加入队头，并记录到这一步的值
            if 0 <= x < n and 0 <= y < m and not maze[x][y] and mark[x][y] == -1:
                queue.append([x, y])
                mark[x][y] = mark[cur[0]][cur[1]] + 1

    return mark[n - 1][m - 1]


maze = [list(map(int, input().split())) for _ in range(n)]
mark = [[-1] * m for _ in range(n)]

print(dfs())

