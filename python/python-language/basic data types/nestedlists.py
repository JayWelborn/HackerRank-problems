if __name__ == '__main__':
    student_data = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data[name] = score
    
    student_grades = sorted(set(student_data.values()))
    
    second_lowest = []
    for key, value in student_data.items():
        if value == student_grades[1]:
            second_lowest.append(key)
            
    for student in sorted(second_lowest):
        print(student)
