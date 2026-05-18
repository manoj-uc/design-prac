# 🐍 Python Coding Standards

## 1. Naming Conventions

| Type              | Convention      | Example                  |
|-------------------|----------------|--------------------------|
| Class Names       | PascalCase     | `StudentManager`         |
| Function Names    | snake_case     | `calculate_total()`      |
| Variable Names    | snake_case     | `student_name`           |
| Constants         | UPPER_CASE     | `MAX_SIZE = 100`         |
| Private Members   | _snake_case    | `_count`                 |

---

## 2. Class Documentation Standards

Every class must include a multi-line docstring describing:

- Purpose of the class  
- Arguments (`Args`)  
- Return values (`Returns`) (if applicable)

### Example

class Student:
    """
    Represents a student object.

    Args:
        student_name (str): Name of student
        student_age (int): Age of student

    Returns:
        None
    """

    def __init__(self, student_name: str, student_age: int) -> None:
        self.student_name = student_name
        self.student_age = student_age

---

## 3. Function Documentation Standards

Every function must include a docstring.

### Example

def calculate_total(price: int, quantity: int) -> int:
    """
    Calculate total amount.

    Args:
        price (int): Product price
        quantity (int): Number of items

    Returns:
        int: Total amount
    """
    return price * quantity

---

## 4. Object Variable Naming Standard

<class_name>_obj

Example:
student_obj = Student()
employee_obj = Employee()

---

## 5. Collection Variable Naming Standard

student_name_list = ["John", "Sam"]

student_details_dict = {
    "name": "John",
    "age": 20
}

student_data_tuple = ("John", 20)

student_id_set = {101, 102, 103}

---

## 6. Maximum Line Length

- Maximum 119 characters per line

---

## 7. Spacing Rules

- 2 blank lines between classes
- 1 blank line between functions

---

## 8. Indentation

- Use 4 spaces
- Avoid tabs

---

## 9. Type Hints

def add(num1: int, num2: int) -> int:
    return num1 + num2

---

## 10. Avoid Hardcoding

MINIMUM_AGE = 18

---

## 11. Class-Level Constants

class Student:
    COLLEGE_NAME = "ABC College"
    TOTAL_STUDENTS = 0

---

## 12. Exception Handling

try:
    value = int(input())
except ValueError:
    print("Invalid input")

---

## 13. Remove Unused Code

- Remove unused imports
- Remove commented code

---

## 14. Best Practices

- Follow DRY
- Use meaningful names
- Use Git

---

## Reference

https://peps.python.org/pep-0008/