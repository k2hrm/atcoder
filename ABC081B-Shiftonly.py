def isEven(i):
  if i % 2 ==0:
    return True
  else:
    return False

i = int(input())
num_row = map(int, input().split())
num_row = list(num_row)
counter = float("inf")
newCounter = 0
for num in num_row:
  newCounter = 0
  while True:
    if isEven(num):
      num = num / 2
      newCounter +=1
    else:
      if newCounter < counter:
        counter = newCounter
      break
print(counter)