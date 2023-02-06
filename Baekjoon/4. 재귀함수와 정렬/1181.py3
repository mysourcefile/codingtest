n = int(input())
arr = [str(input()) for _ in range(n)]

arr = list(set(arr))

arr_word = []
for i in arr:
    arr_word.append([len(i),i])
    
arr_word.sort()

for len_word,word in arr_word:
    print(word)