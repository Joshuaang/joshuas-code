'''
The minimum height a person can be to attend a rock-climbing trip is 1.5 meters

The following program checks whether a person meets the minimum height requirement.

The program allows the user to enter the names and heights of 10 people. 
It will display a message after each person's details are input,
to indicate if the person is tall enough or not.

number_people = 10
minimum_height = 1.5
for x in range(number_people):
  name = input('Name of person: ')
  height = float(input('Height of person: '))
  if height >= minimum_height:
    print('Person is tall enough')
  else:
    print('Person is not tall enough')

Open the file CHECKHEIGHT.py
Save the file as MYCHECKHEIGHT_2021_<your name>_<center_number>_<index number>.py

Question 1:
Edit the program so that it will work for any number of people. 
The program must display a suitable input message.

Save your program.
######################################

Question 2:
A person must be 16 years or older to be old enough to attend a rock-climbing trip.

Edit the program so that it checks that a person is tall enough and old enough to attend
the rock climbing trip. The program must display:
- "The person is not old enough." - if a person is tall enough but not old enough
- "The person is not tall enough." - if a person is old enough but not tall enough
- "The person is not old enough and not tall enough" - if a person is both not old enough and tall enough
- "The person is tall enough and old enough" - if a person is tall enough and old enough

Save your program

###########################################

Question 3:
Edit the program so that it stores the name of the person in a list, 
only if the person is old enough and tall enough.
Each name must be stored in the next available element in the list.

Output the list after all people have been entered.

Save your program as CHECKAGEHEIGHT_2021_<your name>_<center_number>_<index number>.py

'''
#Question 1
# number_people = 10
# minimum_height = 1.5
# for i in range(number_people):
#   name = input('Name of person: ')
#   height = float(input('Height of person: '))
#   if height >= minimum_height:
#     print(f'{name} is tall enough')
#   else:
#     print(f'{name} is not tall enough')

#Question 2
# number_people = 10
# minimum_height = 1.5
# minimum_age = 16
# for i in range(number_people):
#   name = input('Name of person: ')
#   height = float(input('Height of person: '))
#   age = int(input('Age of person: '))
#   if height >= minimum_height:
#     print(f'{name} is tall enough')
#   if age >= minimum_age:
#     print(f'{name} is old enough')
#   if height < minimum_height:
#     print(f'{name} is not tall enough')
#   if age< minimum_age:
#     print(f'{name} is not old enough')

#Question 3
# number_people = 10
# minimum_height = 1.5
# minimum_age = 16
# old = []
# new = []
# for i in range(3):
#   name = input('Name of person: ')
#   height = float(input('Height of person: '))
#   age = int(input('Age of person: '))
#   old.append(name)
#   if height >= minimum_height:
#     print(f'{name} is tall enough')
#   if age >= minimum_age:
#     print(f'{name} is old enough')
#   if height < minimum_height:
#     print(f'{name} is not tall enough')
#   if age< minimum_age:
#     print(f'{name} is not old enough')
#   if age >= minimum_age and height >= minimum_height:
#     new.append(name)
# print(old)
# print(new)