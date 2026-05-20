class Student:
    school_name = "IMAGIINE-VrajMD"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        return sum/len(self.marks)


    def grade(self):
       
        if self.average() > 90:
            return "A"
        elif self.average() < 90 and self.average()>75:
            return "B"
        elif self.average() <75 and self.average()>50:
            return "C"
        else:
            return "D"
        

    def __str__(self):
        
        return f'''Name:{self.name}
                   Average:{self.average()}
                   Grade:{self.grade()}
                   School Name:{self.school_name}
        '''

        


# ------------------------
# Testing the class below
# ------------------------

if __name__ == "__main__":
    s1 = Student("Alice", [85, 90, 88])
    s2 = Student("Bob", [60, 70, 65])

    print(s1) 
    print(s2)