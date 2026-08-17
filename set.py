# 1.	Write a Python program to create a set containing five integers and display all its elements.
integers = {1, 2, 3, 4, 5}
for i in integers:
    print(i)

# 2.	Create a list containing duplicate values. Convert the list into a set and display the resulting set.
duplicate_list = [1, 2, 2, 3, 3, 4, 4, 5, 5]
unique_set = set(duplicate_list)
print(unique_set)

# 3.	Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"apple", "banana", "orange", "grape", "kiwi"}
fruits.add("mango")
fruits.add("pineapple")
print(fruits)

# 4.	Create a set of numbers and remove a specified number from the set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)

# 5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Jarvis", "Sam", "Pushi", "Rushi", "Sankulisa"}
user_input = input("Enter a student name: ")
if user_input in students:
    print(f"{user_input} exists in the set.")
else:
    print(f"{user_input} does not exist in the set.")

# 6.	Create a set of cities and determine the total number of cities using an appropriate function.

cities = {"New York", "London", "Mumbai", "Pune", "Kolhapur"}
total_cities = len(cities)
print(f"Total number of cities: {total_cities}")

# 7.	Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C++", "JavaScript", "Ruby"}
for lang in languages:
    print(lang)

# 8.	Create a list containing duplicate numbers, use a set to remove the duplicates.
duplicate_numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
unique_numbers = set(duplicate_numbers)
print(unique_numbers)

# 9.	Create two sets of integers and find their union.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(union_set)

# 10.	Create two sets and find the elements common to both sets.
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
common_elements = setA.intersection(setB)
print(common_elements)

#11.	Create two sets and find:
# •	Elements present in the first set but not the second 
# •	Elements present in the second set but not the first

setX = {1, 2, 3, 4, 5}
setY = {4, 5, 6, 7, 8}
elements_only_in_X = setX.difference(setY)
elements_only_in_Y = setY.difference(setX)
print(f"Elements only in setX: {elements_only_in_X}")
print(f"Elements only in setY: {elements_only_in_Y}")

# 12.	Create two sets of numbers and find the elements that are present in either set but not in both.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_difference = set1.symmetric_difference(set2)
print(f"Elements in either set but not in both: {symmetric_difference}")

# 13.	Create two sets and determine whether the first set is a subset of the second set.
setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
is_subset = setA.issubset(setB)
print(f"Is setA a subset of setB? {is_subset}")

# 14.	Create two sets and determine whether the first set is a superset of the second set.
setC = {1, 2, 3, 4, 5}
setD = {2, 3}
is_superset = setC.issuperset(setD)
print(f"Is setC a superset of setD? {is_superset}")

# 15.	Write a program to determine whether two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 3}
have_no_common_elements = set1.isdisjoint(set2)
print(f"Do the sets have no elements in common? {have_no_common_elements}")

# Question: Write a Python program to create a set containing five integers and display all its elements.

numbers = {10, 20, 30, 40, 50}

for num in numbers:
    print(num)

# Question: Create a list containing duplicate values. Convert the list into a set and display the resulting set.

numbers = [10, 20, 20, 30, 30, 40, 50, 50]

numbers_set = set(numbers)

print(numbers_set)

# Question: Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print(fruits)

# Question: Create a set of numbers and remove a specified number from the set.

numbers = {10, 20, 30, 40, 50}

numbers.remove(30)

print(numbers)

# Question: Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.

students = {"Amit", "Rahul", "Priya", "Sneha", "Rohan"}

name = input("Enter student name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")

# Question: Create a set of cities and determine the total number of cities using an appropriate function.

cities = {"Mumbai", "Pune", "Delhi", "Chennai", "Kolkata"}

print("Total number of cities:", len(cities))

# Question: Create a set of programming languages and display each language using a for loop.

languages = {"Python", "Java", "C", "C++", "JavaScript"}

for language in languages:
    print(language)

# Question: Create a list containing duplicate numbers, use a set to remove the duplicates.

numbers = [10, 20, 20, 30, 30, 40, 50, 50]

unique_numbers = set(numbers)

print(unique_numbers)

# Question: Create two sets of integers and find their union.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)

print(union_set)

# Question: Create two sets and find the elements common to both sets.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = set1.intersection(set2)

print(common_elements)

# Question: Create two sets and find:
# • Elements present in the first set but not the second
# • Elements present in the second set but not the first

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

first_only = set1.difference(set2)
second_only = set2.difference(set1)

print("Elements in first set but not second:", first_only)
print("Elements in second set but not first:", second_only)

# Question: Create two sets of numbers and find the elements that are present in either set but not in both.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

result = set1.symmetric_difference(set2)

print(result)

# Question: Create two sets and determine whether the first set is a subset of the second set.

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))

# Question: Write a program to determine whether two sets have no elements in common.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))

# Question: Create two sets and check whether they are equal.

set1 = {1, 2, 3, 4, 5}
set2 = {5, 4, 3, 2, 1}

print(set1 == set2)

# Question: Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.

student1 = {"Maths", "Physics", "Chemistry", "English"}
student2 = {"Biology", "Physics", "English", "Computer Science"}

common_subjects = student1.intersection(student2)

print("Subjects studied by both students:", common_subjects)

# Question: Accept a sentence from the user and use a set to display all unique words.

sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:", words)

# Question: Create two sets:
# • Students present in the morning session
# • Students present in the afternoon session
# Find:
# • Students present in both sessions
# • Students present only in the morning
# • Students present only in the afternoon
# • Students present in at least one session

morning = {"Amit", "Rahul", "Priya", "Sneha"}
afternoon = {"Priya", "Sneha", "Rohan", "Karan"}

both = morning.intersection(afternoon)
morning_only = morning.difference(afternoon)
afternoon_only = afternoon.difference(morning)
at_least_one = morning.union(afternoon)

print("Students present in both sessions:", both)
print("Students present only in the morning:", morning_only)
print("Students present only in the afternoon:", afternoon_only)
print("Students present in at least one session:", at_least_one)

# 20. Create sets representing students enrolled in:
# Python
# Java

python_students = {"Amit", "Rahul", "Priya", "Sneha", "Neha"}
java_students = {"Rahul", "Priya", "Karan", "Vikram", "Neha"}

print("Python students:", python_students)
print("Java students:", java_students)

# 21. Find students enrolled in both courses and students enrolled in only one course.

python_students = {"Amit", "Rahul", "Priya", "Sneha", "Neha"}
java_students = {"Rahul", "Priya", "Karan", "Vikram", "Neha"}

both_courses = python_students & java_students
only_one_course = python_students ^ java_students

print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)

# 22. Create two sets representing technical skills of two employees. Find:
# Common skills
# Skills unique to Employee 1
# Skills unique to Employee 2
# All available skills

employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

common_skills = employee1 & employee2
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1 | employee2

print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)

# 23. Create a set containing available books and another set containing requested books. Determine which requested books are available.

available_books = {"Python Basics", "Java Programming", "Data Science", "Web Development"}
requested_books = {"Python Basics", "Machine Learning", "Data Science"}

available_requested = available_books & requested_books

print("Requested books that are available:", available_requested)

# 24. Store visitor IDs from two different days in separate sets. Determine:
# Unique visitors across both days
# Returning visitors
# Visitors who came only on the first day
# Visitors who came only on the second day

day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {103, 104, 105, 106, 107}

unique_visitors = day1_visitors | day2_visitors
returning_visitors = day1_visitors & day2_visitors
first_day_only = day1_visitors - day2_visitors
second_day_only = day2_visitors - day1_visitors

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", first_day_only)
print("Visitors only on second day:", second_day_only)

# Create sets representing products belonging to different categories. Find products that belong to both categories.

electronics = {"Laptop", "Mobile", "Headphones", "Smartwatch"}
gadgets = {"Mobile", "Headphones", "Camera", "Smartwatch"}

common_products = electronics & gadgets

print("Products belonging to both categories:", common_products)

# 25. Represent the friends of two users using sets. Find:
# Mutual friends
# Friends unique to User 1
# Friends unique to User 2
# Total unique friends

user1_friends = {"Amit", "Rahul", "Priya", "Sneha", "Karan"}
user2_friends = {"Rahul", "Priya", "Neha", "Vikram", "Karan"}

mutual_friends = user1_friends & user2_friends
unique_user1 = user1_friends - user2_friends
unique_user2 = user2_friends - user1_friends
total_unique_friends = user1_friends | user2_friends

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique_friends)