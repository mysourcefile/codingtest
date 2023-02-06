n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    m = int(input())
    while cur<=m:
        stack.append(cur)
        answer.append('+')
        cur+=1
    if stack[-1] == m:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break;
if flag == 0:
    for i in answer:
        print(i)