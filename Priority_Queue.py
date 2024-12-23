#優先度付きキュー
import heapq

N,K = map(int,input().split())
P = list(map(int,input().split()))

q = P[:K]
heapq.heapify(q)
print(q[0])

for p in P[K:]:
  if q[0] < p:
    heapq.heappop(q)
    heapq.heappush(q,p)
  print(q[0])