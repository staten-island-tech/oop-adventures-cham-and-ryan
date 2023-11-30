class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def information(self):
        print(f"{self.name}, {self.subject}")