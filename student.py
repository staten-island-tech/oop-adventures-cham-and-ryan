class Student():
    def __init__(self, name, grades, hos):
        self.name = name
        self.grades = grades
        self.hos = hos

    def upgrade(self):
        self.grades += 5
        return self

    def degrade(self):
        self.grades = self.grades - 5
        print(self.grades)
    
    def uphos(self):
        self.hos += 5
        return self
    
    def downhos(self):
        self.hos = self.hos - 5
        return self
    
    def info(self):
        print(f"{self.name}, {self.grades}, {self.hos}")