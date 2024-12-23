#二分探索木
import bisect

n,t = map(int,input().split())
s = input()
x = list(map(int,input().split()))


l = 0
toL = []
toR = []

for i in range(n):
  if s[i] == '0':
    toL.append(x[i])
  else:
    toR.append(x[i])

toL.sort()
result = 0
for e in toR:
  count = bisect.bisect_right(toL, e + 2*t) - bisect.bisect_left(toL,e)
  result += count

print(result)