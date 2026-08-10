# 1.Write a Python program to create a list of five fruits and display the list.

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

print("List of fruits:", fruits)

# ------------------------------------------------------------------------------

# 2. Create a list of five integers. Display:
# •	First element 
# •	Last element 
# •	Third element

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])

print("Last element:", numbers[-1])

print("Third element:", numbers[2])

# -----------------------------------------------------------------------------

# 3. Create a list of colors. Replace the third color with another color and display the updated list.

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

colors[2] = "Orange"

print("Updated list:", colors)

# -----------------------------------------------------------------------------

# 4.	Create a list of numbers. Add:
# •	One element at the end 
# •	One element at the beginning 
# •	One element at a specified position 

number = [10, 20, 30, 40]

number.append(50)

number.insert(0, 5)

number.insert(3, 25)

print("Updated list:", number)



# 5.	Create a list of student names. Remove:
# •	First student 
# •	Last student 
# •	A specific student by name 

students = ["Sanket", "Aryan", "Rushikesh", "Aditya", "Parshwa", "Samarth"]

students.pop(0)

students.pop()

students.remove("Rushikesh")

print("Updated List: ", students)

#  6.	Write a program to find the largest and smallest number in a list without using max() or min().

list_of_numbers = [10, 5, 20, 15, 30]

largest = list_of_numbers[0]
smallest = list_of_numbers[0]


for num in list_of_numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


# 7.	Accept 10 numbers from the user and store them in a list. Calculate:
# sum
# average

Numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    Numbers.append(num)

total = 0
for num in Numbers:
    total += num

average = total / 10

print("Sum:", total)
print("Average:", average)

# 8. 8.	Store 15 integers in a list. Count how many numbers are:
#•	Even 
#•	Odd

Numbers = []

for i in range(15):
    num = int(input("Enter number: "))
    Numbers.append(num)

even_count = 0
odd_count = 0

for num in Numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# 9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["New York", "Mumbai", "Pune", "Kolhapur", "New Delhi"]

city_name = input("Enter a city name: ").lower()

if city_name in cities:
    print("City found in the list.")
else:
    print("City not found in the list.")


# 10.11.	Create a list of 10 numbers and display:
#   First 5 elements 
# 	Last 5 elements 
#	Middle 4 elements 
#	Alternate elements 
#	Reverse list using slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[-5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list using slicing:", numbers[::-1])

# 12.	Display all elements present at even index positions.

list_of_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Elements at even index positions:", list_of_numbers[::2])

# 13.	Accept 10 numbers and sort them in:
#	Ascending order 
#	Descending order


numbers = []

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

numbers.sort()
print("Numbers in ascending order:", numbers)

numbers.sort(reverse=True)
print("Numbers in descending order:", numbers)

# 14. Create a list containing duplicate values and display only unique elements.

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique elements:", unique)



# 15. Find the second largest element in a list.

numbers = [10, 25, 45, 30, 50, 40]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest element:", largest)
print("Second largest element:", second_largest)

