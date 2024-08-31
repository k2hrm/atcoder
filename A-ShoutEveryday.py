A,B,C = list(map(int,input().split()))
if B < C:
  for i in range(B, C+1):
    if i == A:
      print("No")
      exit()
else:
  for j in range(0, C+1):
    if j == A:
      print("No")
      exit()
    for k in range(B, 24):
      if k == A:
        print("No")
        exit()
print("Yes")