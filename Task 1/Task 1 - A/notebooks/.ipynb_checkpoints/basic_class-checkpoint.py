class Student:
    # Class variable (common for all students)
    school_name = "IMAGIINE"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # list of numbers

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
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "D"

    def __str__(self):
        """
        Return formatted student details when printed.
        """
        return f"Name: {self.name}, Average: {self.average():.2f}, Grade: {self.grade()}, School: {Student.school_name}"


# ------------------------
# Test your class below
# ------------------------

if __name__ == "__main__":
    s1 = Student("Alice", [85, 90, 88])
    s2 = Student("Bob", [60, 70, 65])

    print(s1)
    print(s2)