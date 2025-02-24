# Print all numbers from 1 to 100 using a  for  loop.
# n = 100
# for i in range(1, n+1):
#     print(i)

# for i in range(1, 101):
#     print(i)

# def loop():
#     for i in range(1, 101):
#         print(i)
# loop()

# def loop(n):
#     for i in range(1, n+1):
#         print(i)
# loop(100)

# i = 10
# while i > 0:
#     print(i)
#     i -=  1

# i = 1
# while i != 11:
#     print(i)
#     i +=1


 
# Write a program to print the sum of the first n natural numbers. (n*n+1/ 2) 
# n = int(input())
# natural_numbers = (n*(n+1))/2
# print(natural_numbers)

# def natural_numbers(n):
#     return (n*(n+1))/2
# n = int(input())
# print(natural_numbers(n))

# Print all even numbers between 1 and 50 using a  while loop. 
# i = 1
# while i <= 50:
#     print(i)
#     i+=1

# def loop():
#     i = 1
#     while i <= 50:
#         print(i)
#         i+=1
# loop()

# Write a program to display the multiplication table of a given number. First 20
# n = int(input())
# for i in range(1, 21):
#     print(n, "x", i, "=", n*i )

# Reverse a number using a  while  loop.
# n = int(input())
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse*10 + digit
#     n = n // 10
# print(reverse)

# def reverse_number(n):
#     reverse = 0
#     while n > 0:
#         digit = n % 10
#         reverse = reverse*10 + digit
#         n = n // 10
#     return reverse
# n = int(input())
# print(reverse_number(n))

# Reverse a number using a  while  loop. Also can we get the sum of all the digits. 
# n = int(input())
# reverse = 0
# s = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse*10 + digit
#     n = n // 10
#     s+=digit
# print(s)


# Write a program to count the number of digits in a given number using a  while  loop. 
# i = 0
# s = 0
# n = int(input())
# while i <= n:
#     s += i
#     i += 1
# print(s)

#Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a  while  loop.
# n = int(input())
# while n >= 0 :
#     print("Enter any other number")
#     n = int(input())
# print("You have entered a negative number, Thank you")

# def neg(n):
#     while n >= 0:
#         print("enter any other number")
#         n = int(input())
#     print("Thank you for entering a negative number")
# n = int(input())
# neg(n)

# n = int(input())
# for i in range(0,n+1):
#     if n >= i:
#         print("enter any other number")
#         n = int(input())
# else:
#     print("Thank you for entering a negative number") 

# def neg():
#     n = int(input())
#     while n >= 0:
#         print("Enter any other number")
#         n = int(input())
#     print("Thank you for entering a negative number")
# neg()

 
# Print the first 10 terms of the Fibonacci series using a  for loop. 
# Initialize the first two terms of the Fibonacci series
# a, b = 0, 1
# for i in range(10):
#     print(a)
#     a, b = b, a + b

# n = int(input())
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# fibonacci= [0, 1]
# for i in range(2, 10):
#     fibonacci += [fibonacci[i-1] + fibonacci[i-2]]
# print(fibonacci)

#Check if a given number is a prime number using a for loop. 
# num = int(input())
# # if num <= 1:
# #     print(num, "is not a prime number.")
# # else:
# #     for i in range(2, num):
# #         if num % i == 0:
# #             print(num, "is not a prime number.")
# #             break
# #     else:
# #         print(num, "is a prime number.")

#Write a program to calculate the factorial of a number using a while loop. 
# num = int(input())
# factorial = 1
# if num < 0:
#     print("Not possible")
# else:
#     while num > 1:
#         factorial *= num
#         num -= 1
#     print("The factorial is",factorial )

#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)













    



    


