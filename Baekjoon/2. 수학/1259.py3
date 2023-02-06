num = list(map(int,input()))
cnt = 0
while(num[0]!=0):
    for i in range(len(num)//2):
        if num[i] == num[(len(num)-1)-i]:
            cnt+=1
    if(cnt==len(num)//2):
        print("yes")
    else:
        print("no")
    cnt = 0
    num = list(map(int,input()))