my_str = str(input())
my_str =my_str.upper()
answer_str = ""
set_my_str = list(dict.fromkeys(my_str))
set_my_str.sort()
count_array = [my_str.count(i) for i in set_my_str]
for i in set_my_str:
    if my_str.count(i) == max(count_array):
        answer_str+=i
if len(answer_str) > 1:
    print("?")
else :
    print(answer_str)