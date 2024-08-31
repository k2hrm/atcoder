a, b = map(int, input().split())
result = a * b
amari = result % 2
if amari == 0:
  print("Even")
else:
  print("Odd")