# •	Write a program to input a string and display its length without using the len() function. 

text = input("Enter a string: ")

count = 0
for ch in text:
    count += 1

print("Length of the string is:", count)

# --------------------------------------------------------------------------------------------

# •	Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

text = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)

# ---------------------------------------------------------------------------------

# •	Reverse the given string without using built-in reverse functions. 

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)

# ---------------------------------------------------------------------------------

# •	Check whether the entered string is a palindrome. 

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# --------------------------------------------------------------------------------

# •	Count the number of uppercase and lowercase letters in a string. 

text = input("Enter a string: ")

uppercase = 0
lowercase = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)

# ---------------------------------------------------------------------------------------

# •	Find the number of times a specified character appears in a string. 

text = input("Enter a string: ")
char = input("Enter the character to search: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("The character appears", count, "time(s).")

# ---------------------------------------------------------------------------------------

# •	Remove all spaces from the input string. 

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("String without spaces:", result)

# ------------------------------------------------------------------------------------------

# •	Replace all occurrences of a given character with another character. 

text = input("Enter a string: ")
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")

result = ""

for ch in text:
    if ch == old_char:
        result += new_char
    else:
        result += ch

print("Updated string:", result)

# --------------------------------------------------------------------

# •	Print the first and last character of a string. 

text = input("Enter a string: ")

if text == "":
    print("The string is empty.")
else:
    print("First character:", text[0])
    print("Last character:", text[-1])

# ------------------------------------------------------------------

# •	Display each character of a string along with its ASCII value.

text = input("Enter a string: ")

for ch in text:
    print(ch, ":", ord(ch))

# ----------------------------------------------------------------

# Count the total number of words in a sentence.

sentence = input("Enter a sentence: ")

count = 0
in_word = False

for ch in sentence:
    if ch != " " and not in_word:
        count += 1
        in_word = True
    elif ch == " ":
        in_word = False

print("Total number of words:", count) 

# ---------------------------------------------------------------------

# Find the longest word in a given sentence. 

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length:", len(longest))

# ---------------------------------------------------------------------

# Find the shortest word in a sentence. 

sentence = input("Enter a sentence: ")

words = sentence.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)
print("Length:", len(shortest)) 

# -------------------------------------------------------------------

# Convert the first letter of every word to uppercase. 

sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print("Updated sentence:", result)

# -------------------------------------------------------------------------

