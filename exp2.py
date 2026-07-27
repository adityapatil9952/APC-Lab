#looping

#while loop 
i=1
while i<=10:
    print(i,end=" ")
    i+=1


#for loop
print("\nstring iteration")
s="Greeks"
for i in s:
    print(i)


#if statement

num=int(input("Enter a number"))
if num % 2==0:
    print("The given no is even number")

#if - else statement

num=int(input("Enter a Number"))
if num % 2==0:
    print("The Given No is Even Number")
else:
    print("The given no is odd number")

#while with else

i=1
while i<=10:
    print(i,end=" ")
    i+=1
else:
    print("End of the list")


#for with else

tuple=(3,4,6,8,9,2,3,8,9,7)
for value in tuple:
    if value%2!=0:
        print(value)
    else:
        print("These are the odd numbers present in the tuple")


#for loop with range keyword
x=range(3,6)
for n in x:
    print(n)

#Branching or Jumping statements

# 1) break statement

for string in "Python Loop":
    if string=='L':
        break
    print("Current Letter :")

# 2) Continue Statement

for string in "Python Loops":
    if string=="0" or string=="L":
        continue
    print("current Letter :" ,string)


# Pass statement 

def pass_example():
    for i in range(0,10):
        pass
    print("Good Bye!")
pass_example()

#sequence program

def sum_of_two_no():
    num1=1.5
    num2=6.3
    sum=float(num1)+float(num2)
    print("The sum is :",sum)
sum_of_two_no() 



    