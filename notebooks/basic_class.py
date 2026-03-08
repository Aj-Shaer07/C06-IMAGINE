class Student:
	school_name="IMAGINE"
	def __init__(self, name, marks):
		self.name=name
		self.marks=marks

	def average(self):
		return sum(self.marks)/len(self.marks)

	def grade(self):
		t_marks=self.average()
		if t_marks>90: return "A"
		elif t_marks>75: return "B"
		elif t_marks>50: return "C"
		else: return "D"

	def __str__(self):
		 return f"Name: {self.name}, Average: {self.average()}, Grade: {self.grade()}, School: {self.school_name}"

#test class
if __name__ == "__main__":
	s1 = Student("Alice",[85, 90, 88])
	s2 = Student("Bob", [60, 70, 65])
	print(s1)
	print(s2)
