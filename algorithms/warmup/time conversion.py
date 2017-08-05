from time import strptime, strftime

def timeConversion(s):
    # Complete this function
    time = strptime(s, "%I:%M:%S%p")
    return strftime("%H:%M:%S", time)

s = input().strip()
result = timeConversion(s)
print(result)
