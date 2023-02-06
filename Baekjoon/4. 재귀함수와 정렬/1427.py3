num = input()
num_list = []
for i in num:
    num_list.append(int(i))
num_list.sort(reverse = True)
for i in num_list:
    print(i,end="")