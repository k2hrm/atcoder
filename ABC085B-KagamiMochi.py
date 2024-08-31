N = int(input())
a = []
t = int(0)
for i in range(N):
  a.append(int(input()))
  
s=list(set(a))
print(len(s))