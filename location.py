class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def increase_grade(self):
        self.grade += 5

    def decrease_grade(self):
        self.grade -= 5
    
    def info(self):
        print(f"{self.name}, {self.grade}")
