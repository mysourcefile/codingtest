a = input()

answer=''
flag = 0

for i in range(len(a)):
    if a[i]=='X':
        answer+=a[i]
        if len(a)-1==i:
            if answer.count('X')%2==0:
                if answer.count('X')==4:
                    answer = answer.replace('XXXX','AAAA')
                else:
                    answer = answer.replace('XX','BB')
            else:
                flag=1
                print(-1)
            break;
        if answer.count('X')==4:
            answer = answer.replace('XXXX','AAAA')
    elif a[i]=='.':
        answer+=a[i]
        if answer.count('X')%2==0:
            answer = answer.replace('XX','BB')
        else:
            flag=1
            print(-1)
            break;
    
    
if flag == 0:
    print(answer)