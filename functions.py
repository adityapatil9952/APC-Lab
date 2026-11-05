# 1. Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


n = int(input("Enter a number: "))
print(check_even_odd(n))


# 3. Define a function that accepts two numbers and returns the greater number.

def greater(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = greater(num1, num2)
print("Greater number is:", result)


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time(year(s)): "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)


# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

print(is_prime(n))


# 6. Define a function to calculate the area of a circle using its radius.

import math

def circle_area(r):
    area = math.pi * r * r
    return area

radius = float(input("Enter radius: "))

result = circle_area(radius)

print("Area of circle =", result)


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.

def sum_natural(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

result = sum_natural(n)

print("Sum =", result)


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.

def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = power(base, exponent)

print("Result =", result)


# 9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

numbers = [10, 25, 7, 45, 18]

result = find_largest(numbers)

print("Largest element =", result)


# 10. Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(string):
    count = 0

    for ch in string:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

text = input("Enter a string: ")

result = count_vowels(text)

print("Number of vowels =", result)


# 11. Write a function that accepts a string and returns its reverse.

def reverse_string(string):
    reverse = ""

    for ch in string:
        reverse = ch + reverse

    return reverse

text = input("Enter a string: ")

result = reverse_string(text)

print("Reversed string =", result)


# 12. Create a function that checks whether a given string or number is a palindrome.

def is_palindrome(value):
    value = str(value)

    reverse = ""

    for ch in value:
        reverse = ch + reverse

    return value == reverse

value = input("Enter a string or number: ")

if is_palindrome(value):
    print("Palindrome")
else:
    print("Not Palindrome")


# 13. Write a function that accepts a list of numbers and returns their average.

def calculate_average(numbers):
    total = 0

    for num in numbers:
        total = total + num

    average = total / len(numbers)

    return average

numbers = [10, 20, 30, 40, 50]

result = calculate_average(numbers)

print("Average =", result)


# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.

def count_occurrences(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10, 40]
element = int(input("Enter element to search: "))

result = count_occurrences(numbers, element)

print("Number of occurrences =", result)


# 15. Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique

numbers = [10, 20, 10, 30, 20, 40, 10]

result = unique_elements(numbers)

print("Unique elements =", result)


# 16. Create a function to find the second-largest number in a list.

def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

numbers = [10, 25, 7, 45, 18]

result = second_largest(numbers)

print("Second largest =", result)


# 17. Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    result = []

    a = 0
    b = 1

    for i in range(n):
        result.append(a)

        a, b = b, a + b

    return result

n = int(input("Enter n: "))

print("Fibonacci numbers:", fibonacci(n))


# 18. Create a function that accepts marks in five subjects and returns the student's percentage and grade.

def calculate_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

percentage, grade = calculate_result(m1, m2, m3, m4, m5)

print("Percentage =", percentage)
print("Grade =", grade)


# 19. Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.

def electricity_bill(units):

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)

    return bill

units = int(input("Enter units consumed: "))

bill = electricity_bill(units)

print("Electricity Bill = ₹", bill)


# 20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def gross_salary(basic_salary):
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross = basic_salary + hra + da

    return gross

basic = float(input("Enter basic salary: "))

result = gross_salary(basic)

print("Gross Salary =", result)


# 21. Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def calculate_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + (prices[i] * quantities[i])

    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    return final_bill

prices = [1000, 500, 200]
quantities = [2, 1, 3]

result = calculate_bill(prices, quantities)

print("Total Bill =", result)


# 22. Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def calculate_values(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for num in numbers:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

        total = total + num

    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = [10, 25, 5, 40, 20]

minimum, maximum, total, average = calculate_values(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)


# 23.	Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.

def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total


def calculate_percentage(total):
    return total / 5


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def class_average(students):
    total_percentage = 0

    for student in students:
        total_percentage = total_percentage + student["percentage"]

    return total_percentage / len(students)


def highest_scorer(students):
    highest = students[0]

    for student in students:
        if student["total"] > highest["total"]:
            highest = student

    return highest


def lowest_scorer(students):
    lowest = students[0]

    for student in students:
        if student["total"] < lowest["total"]:
            lowest = student

    return lowest


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Name: ")
    roll = input("Roll number: ")

    marks = []

    for j in range(5):
        mark = float(input("Enter marks of subject " + str(j + 1) + ": "))
        marks.append(mark)

    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

print("\n========== STUDENT RECORDS ==========")

for student in students:
    print("\nName       :", student["name"])
    print("Roll No.   :", student["roll"])
    print("Marks      :", student["marks"])
    print("Total      :", student["total"])
    print("Percentage :", student["percentage"])
    print("Grade      :", student["grade"])

average = class_average(students)

print("\nClass Average =", average)

highest = highest_scorer(students)

print("\nHighest Scorer:")
print("Name :", highest["name"])
print("Roll :", highest["roll"])
print("Total:", highest["total"])

lowest = lowest_scorer(students)

print("\nLowest Scorer:")
print("Name :", lowest["name"])
print("Roll :", lowest["roll"])
print("Total:", lowest["total"])


# 24.	Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.

balance = 0
transactions = []


def deposit(amount):
    global balance

    if amount <= 0:
        print("Invalid deposit amount.")
        return

    balance = balance + amount
    transactions.append("Deposited: ₹" + str(amount))

    print("₹", amount, "deposited successfully.")


def withdraw(amount):
    global balance

    if amount <= 0:
        print("Invalid withdrawal amount.")
        return

    if amount > balance:
        print("Insufficient balance.")
        return

    balance = balance - amount
    transactions.append("Withdrawn: ₹" + str(amount))

    print("₹", amount, "withdrawn successfully.")


def balance_enquiry():
    print("Current Balance: ₹", balance)


def transaction_history():
    print("\nTransaction History:")

    if len(transactions) == 0:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == 3:
        balance_enquiry()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        print("Thank you for using the banking system.")
        break

    else:
        print("Invalid choice.")


# 25. Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.

books = {}

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    if book_id in books:
        print("Book already exists.")
        return

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

    print("Book added successfully.")


def issue_book():
    book_id = input("Enter book ID to issue: ")

    if book_id not in books:
        print("Book not found.")
        return

    if books[book_id]["available"] == False:
        print("Book is already issued.")
        return

    books[book_id]["available"] = False

    print("Book issued successfully.")


def return_book():
    book_id = input("Enter book ID to return: ")

    if book_id not in books:
        print("Book not found.")
        return

    if books[book_id]["available"] == True:
        print("Book is already available.")
        return

    books[book_id]["available"] = True

    print("Book returned successfully.")


def search_book():
    keyword = input("Enter book title or author to search: ").lower()

    found = False

    for book_id, book in books.items():
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print("\nBook ID:", book_id)
            print("Title:", book["title"])
            print("Author:", book["author"])

            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")

            found = True

    if not found:
        print("No matching book found.")


def display_available_books():
    print("\n===== AVAILABLE BOOKS =====")

    found = False

    for book_id, book in books.items():

        if book["available"]:
            print("\nBook ID:", book_id)
            print("Title:", book["title"])
            print("Author:", book["author"])

            found = True

    if not found:
        print("No books are currently available.")

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        display_available_books()

    elif choice == "6":
        print("Thank you for using the library system.")
        break

    else:
        print("Invalid choice.")


# 