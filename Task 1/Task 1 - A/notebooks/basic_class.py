class Student:
    
    school_name = "IMAGIINE"

    def __init__(self, name, marks):
        
        self.name = name
        self.marks = marks   

    def average(self):
        """
        Return the average of marks.
        """
        return sum(self.marks) / len(self.marks)

    def grade(self):
        """
        Return grade based on average:
        90+  -> A
        75-89 -> B
        50-74 -> C
        Below 50 -> D
        """
        avg = self.average()

        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 50:
            return 'C'
        else:
            return 'D'

    def __str__(self):
        """
        Return formatted student details when printed.
        """
        return f"Name: {self.name}, Average: {self.average():.2f}, Grade: {self.grade()}, School: {Student.school_name}"

if __name__ == "__main__":
    s1 = Student("Alice", [8