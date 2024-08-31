N,A,B = list(map(int,input().split()))
total = int(0)
for i in range(1,N+1):
  digit = sum(map(int,str(i)))
  if A <= digit <= B:
    total += i
    
print(total)