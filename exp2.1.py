# Q) write Python program to print the natural numbers up to n.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)

# Q) Write Python program to print the even numbers up to n.

n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)

# Q) write Python program to print the odd numbers up to n.

n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)

# Q) write the python program to print 1,2,4,8,16,32...N^2.

n = int(input("Enter number of terms: "))

a = 1

for i in range(n):
    print(a, end=" ")
    a = a * 2

