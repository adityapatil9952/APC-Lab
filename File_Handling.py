# 1) Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file. 

# file = open("student.txt", "w")

# file.write("Name: Sanket Angaj\n")
# file.write("Roll Number: 03\n")
# file.write("Branch: Computer Science and Engineering\n")
# file.write("Semester: V\n")

# file.close()

# print("Student details written successfully.")

# **************************************************************
# file = open("student.txt", "w")

# file.write("Name: Sanket Angaj\n")
# file.write("Roll No.: 03\n")
# file.write("Bramch: CSE")
# file.write("Semester: V\n")

# file.close()
# print("Student details written successfully")


# 2) Write a program to open a text file and display its complete contents.

# file = open("student.txt", "r")

# content = file.read()

# print(content)
# file.close()


# **************************************************************

# file = open("Student.txt", "r")

# content = file.read()

# print(content)
# file.close()


# 3) Write a program to append additional student information to an existing file without deleting its previous contents.

# file = open("student.txt", "a")

# file.write("\nName: Chetan Patil\n")
# file.write("Roll Number: 123\n")
# file.write("Branch: Civil Engineering\n")
# file.write("Semester: V\n")

# file.close()

# print("Additional student information added successfully.")
# **************************************************************

# file = open("student.txt", "a")

# file.write("\nName: Chetan Patil\n")
# file.write("Roll No. : 101\n")
# file.write("Branch: Civil\n")
# file.write("Semester: v\n")

# file.close()
# print("Additional student information added successfully")


# 4) Write a program to read a text file line by line and display each line separately.

with open("student.txt", "r") as file:

    for line in file:
        print(line, end="")


# 5) Write a program to count and display the total number of lines present in a text file. 

with open("student.txt", "r") as file:

    count = 0

    for line in file:
        count += 1

print("Total number of lines:", count)

'''
# 6) Write a program to count the total number of words present in a text file. 

with open("student.txt", "r") as file:

    content = file.read()

    words = content.split()

    count = len(words)

print("Total Number of Words:", count)


# 7) Write a program to count the total number of characters in a text file, including spaces.

with open("student.txt", "r") as file:

    content = file.read()

    count = len(content)

print("Total number of characters:", count)


# 8) Write a program to read a text file and display its lines in reverse order. 

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line, end="")


# 9) Read a text file and count the number of vowels and consonants present in the file. 

with open("student.txt", "r") as file:
    content = file.read()

vowels = 0
consonants = 0

for ch in content.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# 10) Read a text file and calculate the number of alphabets, digits, spaces, and special characters.

with open("student.txt", "r") as file:
    content = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# 11)  Read a text file and find the longest word present in the file.

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()
longest_word = max(words, key=len)

print("Longest word:", longest_word)


# 12)  Read a text file and count how many times each word occurs. Display the result using a dictionary. 

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:", word_count)


# 13) Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears. 

word = input("Enter the word to search: ")

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        words = line.split()
        
        if word in words:
            count += words.count(word)
            line_numbers.append(line_number)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)


# 14)  Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file. 

'''