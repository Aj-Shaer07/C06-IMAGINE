# Task 1A – Learning Phase 1 A

Welcome to Task 1 A!

This task will help you build strong foundations in:

- Git & GitHub
- Python basics
- OOPS classes (Just the essentials)
- Jupyter Notebook usage

These are essential for Machine Learning and future projects.

---

## Part 1 : Git & GitHub

### Fork the GitHub Repository

Folow the instructions in the main README.md file to fork the repo.

After Forking the Repository

Go to Your Fork

After clicking Fork, your repo will be:
https://github.com/your-username/C06-IMAGINE

Clone Your Fork (Not the Original) 
git clone https://github.com/your-username/C06-IMAGINE.git

Move into the Project
cd C06-IMAGINE

Create a New Branch
git checkout -b task1A-yourname

Please Note : Do NOT work directly on main.

After Completing Task
```
git add .
git commit -m "Completed Task 1A"
git push origin task1A-yourname
```
Create Pull Request
Go to your fork on GitHub
Click Compare & Pull Request
Submit PR to the original repository

NOTE :
Always check using git remote -v to confirm you cloned your fork and not the original repository.
Use meaningful commit messages.
Learn about .gitignore

---

# Part 2 : Python Setup

### Create Virtual Environment

```bash
python -m venv venv
````

Activate it and install:

```bash
pip install numpy jupyter notebook
```

Create:

```bash
pip freeze > requirements.txt
```

Commit this file.

---

# Part 3 – Jupyter Notebook

Create folder:

notebooks/

### Create a file: task_normalization.py

Write a function to normalize numerical data between 0 and 1.

Normalization formula:

x' = (x - min) / (max - min)

Write a function:

```python
def normalize(data):
    pass
```

### Create a file: basic_loops.py
Write functions for:
* Prime number checker
* List comprehension

```python
# Exercise 1
# Write a function is_prime(n) that returns True if n is prime, otherwise False.

def is_prime(n):
    pass


# Exercise 2
# Using list comprehension, create a function that returns
# the squares of numbers from 1 to n.

def squares_upto_n(n):
    pass


# Exercise 3
# Using list comprehension, return all even numbers from a list.

def get_even_numbers(nums):
    pass


# Exercise 4
# Using your is_prime function, return all prime numbers from 1 to n
# using list comprehension.

def primes_upto_n(n):
    pass


# Exercise 5
# Given a list of strings, return a new list with all words converted to uppercase
# using list comprehension.

def to_uppercase(words):
    pass
 ```

### Create a file: basic_functions.py

Write the following functions:

* Function with default argument
```python
def greet(name, message="Welcome to IMAGIINE"):
    pass
```

Print: Hello <name>, <message>

Call the function:
Once with only name
Once by changing the default message

* Function returning multiple values
Write a function:
```python
def calculate_stats(numbers):
    pass
```
Input: List of numbers
Return:
Sum
Average
Maximum value

* Lambda function
Use lambda to:
Square a number
Example:
square = lambda x: x * x

Use lambda with map() to:
Square all numbers in a list
Example list:
numbers = [1, 2, 3, 4, 5]
Print the result.

### Create a file : basic_class.py
Create a class:

```python
class Student:
    # Class variable (common for all students)
    school_name = "IMAGIINE"

    def __init__(self, name, marks):
        # Private variables
        self.name = name
        self.marks = marks   # Expecting a list of numbers

    def average(self):
        """
        Return the average of marks.
        """
        # TODO: Calculate and return average
        pass

    def grade(self):
        """
        Return grade based on average:
        90+  -> A
        75-89 -> B
        50-74 -> C
        Below 50 -> D
        """
        # TODO: Use average() and return grade
        # Use self.average() inside grade()
        pass

    def __str__(self):
        """
        Return formatted student details when printed.
        """
        # TODO: Return formatted string with:
        # Name, Average, Grade, School Name
        pass


# ------------------------
# Test your class below
# ------------------------

if __name__ == "__main__":
    s1 = Student("Alice", [85, 90, 88])
    s2 = Student("Bob", [60, 70, 65])

    print(s1)
    print(s2)
```

---

## This task is about learning properly.
Do not copy-paste. Try to understand what you write.
Ensure code runs without errors. Keep formatting clean
Be prepared to move into Task 1 - B in Learning Phase 1


