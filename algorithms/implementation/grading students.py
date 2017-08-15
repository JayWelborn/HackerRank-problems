def solve(grades):
    for index, grade in enumerate(grades):
        if grade < 38 or grade % 5 <= 2:
            pass
        else:
            grade = int(round(grade/5) * 5)           
        grades[index] = grade        
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))