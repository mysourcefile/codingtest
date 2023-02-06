x,y = map(int,input().split())
day = 0
week = 0

for i in range(1,x):
    if i%2 == 1:
        if i==9 or i==11:
            day+=30
        else:
            day+=31
    elif i%2 == 0:
        if i == 2:
            day+=28
        elif i== 8 or i == 10 or i == 12:
            day+=31
        else :
            day+=30
day+=y

if day%7 == 0:
    print("SUN")
elif day%7 == 1:
    print("MON")
elif day%7 == 2:
    print("TUE")
elif day%7 == 3:
    print("WED")
elif day%7 == 4:
    print("THU")
elif day%7 == 5:
    print("FRI")
elif day%7 == 6:
    print("SAT")
        