#import prac0723_mod
import idkpy
'''
A class has 10 students. The following program allows a teacher 
to input the favourite color of each students in the class.

num_students = 10
for x in range(num_students):
  colour = input(“What is the student’s favourite colour?”)

Open the file COLOURS.py
Save the file as COLOURS_2022_<your name>_<centre number>_<index number>.py
1.	Edit the program to use a conditional loop that repeats 
until the teacher does not want to enter any more colours. 
Suitable input messages must be used.

Save your program [3]

2.	Edit your program to convert each colour to lower case and 
then store it into a list.

Save your program [2]

3.	Edit your program to display the number of students that 
have a specific favourite colour.

The program must:
a.	Ask the teacher to input a colour to search for in the list.
b.	Output the colour and the number of students who have that 
specific colour as their favourite colour.

Suitable input and output messages must be used.

Save your program. [5]

'''

# #################### Answer for Question 1 ########################
# while True:
#   colour = input("What is the student’s favourite colour? ")
#   if colour == 'stop':
#     break

# #################### Answer for Question 2 ########################
# list1 = []
# while True:
#   colour = input("What is the student’s favourite colour? ")
#   if colour == 'stop':
#     break
#   else:
#     colour = colour.lower()
#     list1.append(colour)    
# print(list1)

# #################### Answer for Question 3 ########################
# list1 = []
# count = 0
# while True:
#   colour = input("What is the student’s favourite colour? ")
#   if colour == 'stop':
#     break
#   else:
#     colour = colour.lower()
#     list1.append(colour)    
# print(list1)
# teacher = input("Which colour do you want to search? ")
# for i in list1:
#   if teacher.lower() == i:
#     count = count + 1
# print(f"There are {count} children whose favourite colour is {teacher}.")


# Write a code to ask for an input and output all the Uppercase letters followed by digits, then the lowercase letters.

# Sample Interaction
# Enter your input: 12A3BabcC
# Answer is ABC123abc

# uppercase = ''
# lowercase = ''
# digits = ''
# word = input("Enter your input: ")
# for i in word:
#   if i.isupper():
#     uppercase = uppercase + i
#   elif i.isdigit():
#     digits = digits + i
#   elif i.islower():
#     lowercase = lowercase + i
# print(f"Answer is {uppercase + digits + lowercase}.")

#  Write a code to accept only the first 5 digits in an input. Replace with * sign if there are less than 5 digits.

# Sample interaction
# Enter your input: abc123456abc
# Answer is 12345

# Enter your input: abd12adfda
# Answer is 12***
# import prac0524
# import prac0621