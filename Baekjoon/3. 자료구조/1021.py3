from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,(input().split()))
list_n = deque(list(range(1,n+1)))
p_num = list(map(int,input().split()))
answer = 0

for i in p_num:
    while True:
        if list_n[0] == i:
            list_n.popleft()
            break;
        else:
            if list_n.index(i) <= len(list_n)//2:
                list_n.rotate(-1)
                answer += 1
            else:
                list_n.rotate(1)
                answer += 1
print(answer)