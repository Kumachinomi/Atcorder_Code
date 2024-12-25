#二分探索・累積和
import bisect

n, s = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
  a.append(a[i])
  
sum_a = [0] * (2 * n + 1)
for i in range(2 * n):
  sum_a[i + 1] = sum_a[i] + a[i]
  

result = False
s %= sum_a[n]
for i in range(2 * n):
  
  it = bisect.bisect_left(sum_a,sum_a[i] + s)
  if it < 2 * n and sum_a[it] == sum_a[i] + s:
    result = True

print("Yes" if result else "No")






#二分探索・累積和 2
import bisect

n,q = map(int,input().split())
r = list(map(int,input().split()))
r.sort()

s = [0] * (n + 1)
s[0] = 0
for i in range(n):
  s[i + 1] = s[i] + r[i]


  
for i in range(q):
  x = int(input())
  it = bisect.bisect_right(s,x)-1
  print(it)