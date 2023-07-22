n, m = map(int, input().split())
N = 1000001
slite = [0] * N
left, right = 0, -1
arr = list(map(int, input().split()))
for i in range(n):
    while left <= right and arr[i] <= arr[slite[right]]:
        right -= 1
    while left <= right and i - m >= slite[left]:
        left += 1
    right += 1
    slite[right] = i
    if i >= m - 1:
        print(arr[slite[left]], end=' ')
print()

left, right = 0, -1
for j in range(n):
    while left <= right and arr[j] >= arr[slite[right]]:
        right -= 1
    while left <= right and j - m >= slite[left]:
        left += 1
    right += 1
    slite[right] = j
    if j >= m - 1:
        print(arr[slite[left]], end=' ')
