from collections import deque
n,m = map(int,input().split())
list_n = deque([i for i in range(1,n+1)])
cnt = 0
answer = []
for i in range(n):
    while cnt!=m-1:
        list_n.rotate(-1)
        cnt+=1
    cnt =0
    answer.append(list_n.popleft())

print("<",end='')
print(', '.join(map(str,answer)), end='')
print(">",end="")
        