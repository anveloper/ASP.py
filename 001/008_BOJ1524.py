n = int(input())
for i in range(n):
  tmp = input()
  n, m = map(int,input().split())
  n = max(list(map(int,input().split())))
  m = max(list(map(int,input().split())))
  if n >= m:
    print("S")
  else:
    print("B")
