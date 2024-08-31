N, K = map(int,input().split())
numbers = list(map(int,input().split()))
f = numbers[:N-K]
l = numbers[N-K:]
new = l + f
print(*new)