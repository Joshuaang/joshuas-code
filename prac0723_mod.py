'''
Algorithm Question:
Given a list of random numbers, Write a program to determine which 
numbers in the list are even or odd. 
'''
# [3, 9, 10, 11, 17, 23, 25, 28, 29, 37, 39, 44, 45, 47, 56, 57, 85, 93, 99]

# nums = [3, 9, 10, 11, 17, 23, 25, 28, 29, 37, 39, 44, 45, 47, 56, 57, 85, 93, 99]
# even = []
# odd = []
# for i in nums:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'Even numbers are {even}')
# print(f'Odd numbers are {odd}')

# # Exercise 1: Points Game
# """
# In this game, players collect points that are added to their total score. 
# The player can only see the last digit of their score on a display. 
# Your task is to write a Python program that takes the player’s total score 
# as input and returns the last digit of the score.

# Example input: 12345
# Expected output: 5

# HINT: Use the modulus operator (%) to find the last digit of the score.
# """
# score = 12345
# print(score % 10)

# # Exercise 2: Circular Seating Arrangement
# """
# You have a circular arrangement of 10 seats numbered from 0 to 9. 
# If you start counting from seat number 0 and wrap around to the beginning 
# after reaching the last seat, what is the student name of the 
# position of the seat you land on if you count up to the 25th position?

# List of students: ** given below**
# Example input: Start from seat number 0, count to the 25th position.
# Expected output: The position of the seat you land on.
# HINT: Use modular arithmetic to solve the problem.
# """
# # Write and test your code here
# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 
#             'Frank', 'Grace', 'Helen', 'Ian', 'Jack']

# Task 1: Get the total number of seats
# count = 23
# total_students = len(students)

# Task 2: Calculate the final position using the modulus operator
# index = (count - 1) % total_students

# Task 3: Retrieve the student's name at the final position
# print("Student at position {} is {}".format(count,students[index]))
# studentname = ''
# for i in range(total_students):
#     if i == index:
#         studentname = students[i]
#         print(studentname)


##### Convert 564 minutes to hours and minutes
# combination of floor division and modulus to do this
hours = 564 // 60
mins = 564 % 60
print(f'hours are {hours}, mins are {mins}')



######### string formatting  #############
### string concatenation --- - joining strings together
name = "John"
age = 18
### My name is John, I am 18 years old

##### option 1: print() and comma, simple, type conversion for you
#strmsg =  # tuple
print("My name is", name, ". I am ", age, "years old.")

###### options 2: use + operator to join, need to handle type conversion
strmsg = "My name is " +  name +  ". I am "+ str(age) + " years old."
print(strmsg)

###### option 3: use f string -- what most programmers use, 
strmsg2 = f"My name is {name}. I am {age} years old."
print(strmsg2)

##### option 4: use "".format() #backward compatible
strmsg3 = "My name is {}, I am {} years old.".format(name, age)
print(strmsg3)