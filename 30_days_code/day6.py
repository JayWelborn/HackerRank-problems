total_words = int(input())

for _ in range(total_words):
    word = input()
    even = word[0::2]
    odd = word[1::2]
   
    print(even + ' ' + odd)