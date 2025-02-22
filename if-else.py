#Write a program to check if a given number is positive, negative, or zero
n=int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

  
# Determine if a number is odd or even
n=int(input())
if n%2 == 0:
    print("Even")
else:
    print("Odd")


#Check if a person is eligible to vote (age >= 18)
age = int(input())
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#Write a program to find the greatest of two numbers. 
a = int(input())
b = int(input())
if a > b:
    print(a , " is greater than " , b)
else:
    print(b , " is greater than " , a)


#Print "pass" if a student if a student scores more than 40 marks otherwise, print "Fail"
passmark = 40
student_score = int(input())
if student_score > 40:
    print("Pass")
else:
    print("Fail")


#Write a program to dispaly the day of a week based on number input { 1 for Monday , 2 for Tuesday...}
user_input = int(input())
if user_input == 1:
    print("Monday")
elif user_input == 2:
    print("Tuesday")
elif user_input == 3:
    print("Wednesday")
elif user_input == 4:
    print("Thursday")
elif user_input == 5:
    print("Friday")
elif user_input == 6:
    print("Saturday")
elif user_input == 7:
    print("Sunday")
else:
    print("There are only 7 days in a week")


# Implement a simple calculator to perform addition, subtraction, multiplication, and division. 
print((lambda x, y, op: x + y if op in ['+', 'add'] else x - y if op in ['-', 'sub'] else x * y if op in ['*', 'mul'] else x / y if op in ['/', 'div'] else "Invalid operator")(float(input("Enter first number: ")), float(input("Enter second number: ")), input("Enter operation (+, -, *, /, add, sub, mul, div): ")))

num1 = float(input())
num2 = float(input())
operation = input().lower()
if operation == '+' or operation == 'add':
    result = num1 + num2
elif operation == '-' or operation == 'sub':
    result = num1 - num2
elif operation == '*' or operation == 'mul':
    result = num1 * num2
elif operation == '/' or operation == 'div':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"
print(result)


# Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.)
print(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(input()) - 1] if 1 <= int(input()) <= 12 else "Invalid month number!")

user_input = int(input())
if user_input == 1:
    print("January")
elif user_input == 2:
    print("February")
elif user_input == 3:
    print("March")
elif user_input == 4:
    print("April")
elif user_input == 5:
    print("May")
elif user_input == 6:
    print("June")
elif user_input == 7:
    print("July")
elif user_input == 8:
    print("August")
elif user_input == 9:
    print("September")
elif user_input == 10:
    print("October")
elif user_input == 11:
    print("November")
elif user_input == 12:
    print("December")
else:
    print("There are only 12 months in a year")


# Write a program to find the greatest of three numbers
a, b, c = map(int, input().split())
if a > b and a > c:
    print(a, " is greatest of all")
elif b > a and b > c:
    print(b, " is the greatest of all")
else:
    print(c, " is the greatest of all")


# Check if a year is a leap year.
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, " is a leap year")
else:
    print(year, " is not a leap year")

def leap(n):
    if (n % 400 ==0) or (n % 4 ==0 and n % 100 != 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
year = int(input())
print(leap(year))


# Write a program to classify a character entered by the user as a vowel, consonant, or neither. 
character = input(" ")
if character in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

def vowel(s):
    if s in "aeiouAEIOU":
        return "Vowel"
    else:
        return "Not a Vowel"
s = input(" ")
print(vowel(s))


# Calculate the grade of a student based on the marks they score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. 
def grade(marks):
    if 90 <= marks <= 100:
        print("Grade A")
    elif 80 <= marks <= 89:
        print("Grade B")
    elif 70 >= marks >= 79:
        print("Grade C")
    elif marks <= 70:
        print("Fail")
    else:
        print("Invalid")
marks = int(input())
grade(marks)


# Write a program to check if three sides length form a valid triangle. 
def triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return "Valid Triangle"
    else:
        return "Not Valid"
a = int(input())
b = int(input())
c = int(input())
print(triangle(a, b, c))

  














    



