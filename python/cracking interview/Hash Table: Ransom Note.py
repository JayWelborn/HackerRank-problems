def ransom_note(magazine, ransom):
    ransom = sorted(ransom)
    magazine = sorted(magazine)
    for word in ransom:
        if word not in magazine:
            return False
        else:
            magazine.remove(word)
    return True


if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")
