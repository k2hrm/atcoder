N = int(input())
numbers = list(map(int,input().split()))
cnt = 0
sums = float('inf')
while sums > 1:
  numbers.sort(reverse=True)
  numbers[0] = numbers[0]-1
  numbers[1] = numbers[1]-1
  sums = 0
  for i in numbers:
    if i > 0:
      sums += 1
  cnt +=1

print(cnt)