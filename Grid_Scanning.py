#事前走査
n = int(input())
s = [input() for i in range(n)]
x = [0] * n
y = [0] * n
for i in range(n):
  for j in range(n):
    if s[i][j] == 'o':
      x[i] += 1
      y[j] += 1


result = 0
for i in range(n):
  for j in range(n):
    if s[i][j] == 'o':
      result += (x[i] - 1) * (y[j] - 1)

print(result)