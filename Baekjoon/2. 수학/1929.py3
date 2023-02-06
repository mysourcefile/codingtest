import math
n,m = map(int,input().split())
def solve(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    
    return True
    
for i in range(n,m+1):
    if solve(i) == True:
        print(i)