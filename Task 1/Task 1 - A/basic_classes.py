#classes
class student:
    school='NITK'
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def grade(self):
        avg=self.average()
        if avg>=90:
            return 'A'
        elif avg>=80:
            return 'B'
        elif avg>=70:
            return 'C'
        elif avg>=60:
            return 'D'
        else:
            return 'F'
    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}, Average: {self.average():.2f}, Grade: {self.grade()}, School: {self.school}"
        
if __name__ == "__main__":
    s1 = student("Alice", [85, 90, 88])
    s2 = student("Bob", [60, 70, 65])

    print(s1)
    print(s2)