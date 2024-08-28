'''
# Exercise 6: Check Even or Odd
# Use an if-else statement to check if a number is even or odd.
# Example input: number = 4
# Expected output: 'The number is even.'
# hint: use the mod %, any number divisible by 2 is even
'''
# Write your code here
num = int(input('Enter a number: '))
if num % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')
    
'''
# Exercise 7: Age Group Classification
# Use if-elif-else statements to classify a person into age groups.
 < 13 = child
 < 20 = teenager
# Example input: age = 25
# Expected output: 'You are an adult.'
'''
# Write your code here
# age = int(input('Enter your age: '))
# if age < 13:
#     print('You are a child.')
# elif 13 <= age < 20:
#     print('You are a teenager.')
# elif age >= 20:
#     print('You are an adult.')

'''
# Exercise 8: Temperature Check
# Use if-elif-else statements to check if a temperature is cold, warm, or hot.
# use your own values to determine what is cold, warm or hot.
# Example input: temperature = 30
# Expected output: 'It is warm.'
'''
# Write your code here
# temp = int(input('Enter temperature: '))
# if temp < 25:
#     print('It is cold.')
# if 25 <= temp < 35 :
#     print('It is warm.')
# if temp >= 35:
#     print('It is hot.')

'''
# Exercise 9: Validating Age Input
# Use if-else statements to validate if the entered age is a positive number.
# Example input: age = -5
# Expected output: 'Invalid age.'
'''
# Write your code here
# age = int(input('Enter your age: ')) 
# if age > 0:
#     print('Valid age.')
# elif age <= 0:
#     print('Invalid age.')

'''
# Exercise 10: Greeting Based on Time
# Use if-elif-else statements to print a greeting based on the time of the day.
# Good morning, Good afternoon, Good evening, Good night
# assume time is based on 24 hour clock, i.e 13 is 1.00pm
# Example input: time = 15
# Expected output: 'Good afternoon.'
'''
# Write your code here
# time = int(input('Enter the time: '))
# if 1 <= time < 12:
#     print('Good morning.')
# elif 12 <= time < 17:
#     print('Good afternoon.')
# elif 17 <= time <  20:
#     print('Good evening.')
# elif 20 <= time <= 24:
#     print('Good night.')

'''
# Exercise 11: Grade Evaluation
# Use if-elif-else statements to evaluate a grade.
>= 90 = A*
>= 80 = A
>= 70 = B
>= 60 = C
anything lesser is a D
# Example input: grade = 85
# Expected output: 'You got an A.'
'''
# Write your code here
# grade = int(input('Enter your grade: '))
# if grade >= 90:
#     print('You got an A*.')
# elif grade >= 80:
#     print('You got an A.')
# elif grade >= 70:
#     print('You got a B.')
# elif grade >= 60:
#     print('You got a C.')
# elif 0 <= grade < 60:
#     print('You got a D.')
# elif grade < 0:   #T.David, this should be an else
#     print('Invalid grade.')
    
'''
# Exercise 12: Boolean Logic
# Assign boolean values to two variables and print the result of their logical AND.
# Example input: is_sunny = True, has_umbrella = False
# Expected output: False
'''
# Write your code here
# is_sunny = True
# has_umbrella = False
# if is_sunny == has_umbrella:
#     print('True')
# else:
#     print('False')

'''
# Exercise 13: Voting Eligibility
# Use if-else statements to check if a person is eligible to vote.
# Example input: age = 17
# Expected output: 'You are not eligible to vote.'
'''
# Write your code here
# age = int(input('Enter your age: '))
# if age < 21:
#     print('You are not eligible to vote.')
# elif age >= 21:
#     print('You are eligible to vote.')

'''
# Exercise 15: Password Validation
# Use if-else statements to check if a password meets a minimum length requirement.
# Example input: password = 'abc123'
# Expected output: 'Password is too short.'
'''
# Write your code here
# minimumlen = 7
# password = input('Enter your password: ')
# if len(password) < minimumlen:
#     print('Password is too short.')
# elif len(password) >= minimumlen:
#     print('Password is suitable.')

######################## LIST #########################
# defining a list
# planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter']

# # how to retrieve values from a list # index
# var1 = planets[4]
# print(var1)

# # change the value of a list item
# planets[0] = 'brandonland'
# print(planets)

# # add an item to this list. .append()
# planets.append('brandonland2')
# print(planets)

# # remove an item from the list by name .remove()
# planets.remove('jupiter')
# print(planets)

# # remove an item by index... using del()
# del(planets[3])
# print(planets)
 
################## LIST EXERCISES #####################
'''
Question 1: Create a list of 4 colors.
expected output:
['red', 'green', 'blue', 'yellow']
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']

'''
Question 2: Access the third element in the list colors = ['red', 'green', 'blue', 'yellow'].
example input:
colors = ['red', 'green', 'blue', 'yellow']
expected output:
'blue'
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# print(colors[2])

'''
Question 3: Add the color 'purple' to the end of the colors list.
example input:
colors = ['red', 'green', 'blue', 'yellow']
expected output:
['red', 'green', 'blue', 'yellow', 'purple']
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# colors.append('purple')
# print(colors)

'''
Question 4: Remove the color 'green' from the colors list.
example input:
colors = ['red', 'green', 'blue', 'yellow']
expected output:
['red', 'blue', 'yellow']
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# colors.remove('green')
# print(colors)

'''
Question 5: Modify the second element of the colors list to 'orange'.
example input:
colors = ['red', 'green', 'blue', 'yellow']
expected output:
['red', 'orange', 'blue', 'yellow']
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# colors[1] = 'orange'
# print(colors)

'''
Question 6: Slice the colors list to get the last four colors.
example input:
colors = ['red', 'green', 'blue', 'yellow']
expected output:
['blue', 'yellow']

list slicing
'''
# colors = ['red', 'green', 'blue', 'yellow','orange', 'purple','pink','cyan']
# Write your code here
# print(colors[4:8])

'''
Question 7: Iterate over the colors list and print each color in uppercase.
example input:
colors = ['red', 'green', 'blue', 'yellow']
expected output:
RED
GREEN
BLUE
YELLOW
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# for i in colors:
#     print(i.upper())

'''
Question 8: delete the item 2 in the list using del()
example input:
colors = ['red', 'blue', 'yellow', 'green']
expected output:
['red', 'yellow', 'green']
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# del colors[1]
# print(colors)

'''
Question 9: Reverse the order of the colors list.
example input:
colors = ['red', 'blue', 'yellow', 'green']
expected output:
['green', 'yellow', 'blue', 'red']
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']

# to reverse, list slicing method - 1 line of code
# print(colors[::-1])

## to reverse using an insert() list function
# print(reversed(colors))
#(I need help with this)

'''
Question 10: Find the length of the colors list.
example input:
colors = ['red', 'blue', 'yellow', 'green']
expected output:
4
'''
# Write your code here
# colors = ['red', 'green', 'blue', 'yellow']
# print(len(colors))

'''
Question 11: Create a list of squares of the first 100 positive integers.
example input:
None
expected output:
[1, 4, 9, 16, 25]
# hint use a for loop

'''
# Write your code here
# squares = []
# for i in range(1,101):
#     squares.append(i**2)
# print(squares)

'''
Question 12: Write a function that takes a list of numbers and 
returns a new list with the square of each number.
example input:
[11, 2232, 3323, 44345, 5566]
expected output:
[121, 4, 9, 16, 25]
'''
# Write your code here
# lst = [13, 12, 69, 421, 10]
# newlst = []
# for i in lst:
#     newlst.append(i**2)
# print(newlst)

'''
Question 13: Given a list of words, create a new list of words that are 
longer than 3 characters.
example input:
['tree', 'car', 'house', 'sun', 'computer','table']
expected output:
['tree', 'house', 'computer']
'''
# Write your code here
# lst = ['tree', 'car', 'house', 'sun', 'computer','table']
# newlst = []
# for i in lst:
#     if len(i) > 3:
#         newlst.append(i)
#     elif len(i) <= 3:
#         pass
# print(newlst)

'''
Question 14: Write a function that takes a list of numbers and 
returns the sum of the even numbers in the list.
example input:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expected output:
30
'''
# Write your code here
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evenlst = []
# sum = 0
# for i in lst:
#     if i % 2 == 0:
#         evenlst.append(i)
#     elif i % 2 != 0:
#         pass
# for i in evenlst:
#     sum += i
# print(sum)