class student:
    """класс для описания студентов"""
    name=''
    age=''
    grades=[]
    middle=int
    def __init__(self, name: str ='', age: str =''):
        self.name
        self.age
    def add_grade(self):
        add=int(input('оценка :'))
        self.grades.append(add)
        while add!=0:
            add = int(input('оценка :'))
            self.grades.append(add)
    def mid(self):
        summary=0
        for i in self.grades:
            summary+=(i)
            self.middle=summary/len(self.grades)
        return self.middle


    def is_exelent(self):
        if self.middle>4.5:
            return True
        else:
            return False





