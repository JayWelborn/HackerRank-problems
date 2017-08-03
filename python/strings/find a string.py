def count_substring(string, sub_string):
    count = start = 0
    while start >= 0:
        position = string.find(sub_string, start)
        if position < 0:
            break
        count += 1
        start = position + (len(sub_string) // 2)
        
    return count