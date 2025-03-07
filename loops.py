# # Write a program to display the multiplication table of a given number. First 20
n = int(input())
for i in range(1, 21):
    print(n, "x", i, "=", n*i )

def mul(n):
    for i in range(1, 21):
        print(n, "x", i, "=", n*i )
n = int(input())
mul(n) 

# #Write a program to calculate the factorial of a number using a while loop. 
num = int(input())
factorial = 1
if num < 0:
    print("Not possible")
else:
    while num > 1:
        factorial *= num
        num -= 1
    print("The factorial is",factorial )

def factorial(n):
    fact = 1
    if n < 0:
        print("Not possible")
    else:
        while n > 1:
            fact *= n
            n -= 1
        print("The factorial is", fact) 
n = int(input("Enter a number: "))
factorial(n)  


# #Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

def div():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
div()













    



    


