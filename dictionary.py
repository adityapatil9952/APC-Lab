# 1.	Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.

student = {
    "roll_number": 7,
    "name": "Aditya",
    "department": "CSE",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# 2.	Create a dictionary containing employee information and display the value associated with a specified key.

employee = {
    "employee_id": 9999,
    "name": "Sanku lisa",
    "department": "cse",
    "salary": 5
}

key_to_display = "name"  
if key_to_display in employee:
    print(key_to_display, ":", employee[key_to_display])
else:
    print("Key not found.")

# 3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "product1": 100,
    "product2": 200,
    "product3": 300,
    "product4": 400,
    "product5": 500
}

products["product6"] = 600
print(products)

# 4.	Create a dictionary containing student marks. Update the marks of a specified student.
student_marks = {
    "Sankulisa": 85,
    "Rushi": 90,
    "Pushi": 78
}

student_marks["Sankulisa"] = 95
print(student_marks)

# 5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities = {
    "Pune": 300000,
    "Mumbai": 1200000,
    "Delhi": 1100000,
    "Kolhapur": 350000
}

del cities["Mumbai"]
print(cities)

# 6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees = {
    101: "Sankulisa",
    102: "Rushi",
    103: "Pushi"
}

emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee found:", employees[emp_id])
else:
    print("Employee not found.")
