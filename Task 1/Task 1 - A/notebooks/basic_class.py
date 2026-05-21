class Student:
    school_name = "IMAGINE"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        for i in self.marks:
            if type(i)!=int:
                return 0
        return sum(self.marks)/len(self.marks)
    
    def grade(self):
        avg=self.average()
        if avg>=90:
            return "A"
        elif avg>=75:
            return "B"
        elif avg>=50:
            return "C"
        else:
            return "D"
        
    def __str__(self):
        avg=self.average()
        grd=self.grade()
        return (f"Name: {self.name}\n"
                f"Average: {round(avg,2)}\n"
                f"Grade: {grd}"
                f"School: {Student.school_name}")

if __name__ == "__main__":
    s1 = Student("Alice", [85, 90, 88])
    s2 = Student("Bob", [60, 70, 65])

    print(s1)
    print(s2)        