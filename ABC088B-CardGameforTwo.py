N = int(input())
a = list(map(int,input().split()))
t = 0
cnt = 0
def isOdd(i):
  if i % 2 == 0:
    return False
  else:
    return True

a.sort(reverse=True)
for i in a:
  cnt += 1
  if isOdd(cnt):
    t += i
  else:
    t -= i

print(t)