from itertools import combinations


n,s = map(int,input().split())
count = 0
data = list(map(int,input().split()))

for i in range(1,n+1):
    per = combinations(data,i)
    for j in list(per):
        if sum(j)==s:
            count+=1
print(count)