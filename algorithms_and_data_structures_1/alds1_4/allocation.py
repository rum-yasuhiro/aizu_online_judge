import math

n, k = map(int, input().split())

l = []
for _ in range(n):
    l.append(int(input()))

num_combination = math.comb(n - 1, k - 1)

for _ in range(num_combination):
    pass
