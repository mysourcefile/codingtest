import sys

str_l = list(input())
str_r = []
n = int(input())

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "L" and str_l:
        str_r.append(str_l.pop())
    elif cmd[0] == "D" and str_r:
        str_l.append(str_r.pop())
    elif cmd[0] == "B" and str_l:
        str_l.pop()
    elif cmd[0] == "P":
        str_l.append(cmd[1])

print("".join(str_l + list(reversed(str_r))))
    