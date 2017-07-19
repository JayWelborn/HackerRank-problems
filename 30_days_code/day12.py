class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average_grade = sum(self.scores) / len(self.scores)
        if 90<=average_grade<=100:
            return 'O'
        elif 80<=average_grade<90:
            return 'E'
        elif 70<=average_grade<80:
            return 'A'
        elif 55<=average_grade<70:
            return 'P'
        elif 40 <=average_grade<55:
            return 'D'
        else:
            return 'T'
    