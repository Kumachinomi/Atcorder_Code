#包除原理
def nc2(n):
  return n * (n - 1) // 2
  
n = int(input())
a = list(map(int,input().split()))
b = [[] for _ in range(n)]　# 各数字の出現位置を記録

for i in range(n):
  a[i] -= 1
  b[a[i]].append(i)　# 各数字が出現する位置を記録

result = 0
for i in range(n):
  b[i].append(n)　# 各リストの終端にnを追加
  pre = -1
  result += nc2(n + 1)　# 全体の区間数を加算
  for e in b[i]:
    result -= nc2(e - pre)　# 数字iを含まない区間の数を引く
    pre = e

print(result)