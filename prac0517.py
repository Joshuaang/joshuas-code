# Task 1
# check if string 1 is equal to string 2
# write a program to ask for 2 strings.
# if the two string are exactly the same, print 'same'
# else print 'not same'
# Run and Test your code
# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")
# if s1 == s2:
#     print("same")
# elif s1 != s2:
#     print("not same")

# Task 2
# check if length of string 1 is equal to length of string 2
# write a program to ask for 2 strings.
# if the two string are exactly the length, print 'same'
# else print 'not same'
# Run and Test your code
# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")
# if len(s1) == len(s2):
#   print('same')
# else:
#   print('not same')
# if s1 == s2 or len(s1) == len(s2):
#     print("same")
# elif s1 != s2 or len(s1) == len(s2):
#     print("not same")

# # Task 3
# Modify the code in Task 1, such that it is case insensitive
# Run and Test your code
# HAPPY == happy, # HappY == happy
# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")
# if s1.lower() == s2.lower():
#     print("same")
# else:
#     print("not same")

# Task 4
# Modify the code in Task 2, that if they are the same
# give hints as to which letter between string 1 and string 2 is correct
# Example: if the string 1 is crook, and string 2 is crack it will show c r _ _ k
# Run and Test your code

# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")
# outword = ''
# if len(s1) == len(s2):
#     for i in range(len(s1)):
#         if s1[i] == s2[i]:
#             outword = outword + s1[i]
#         else:
#             outword = outword + ' _ '
# else:
#     print("The words are not the same.")
# print(outword)
 
# string concatenation

# put a temp word which is blank
# loop through every character in the word
  # if character [index] of s1 == character [index] of s2:
      # add character [index] of s1 to temp variable
   #else
      # add " _ " to temp variable

# Task 5a: reversing a string 
# input string is "cockroach", "hcaorkcoc"
# use string slicing
# string = input("Enter a string: ")
# string = string[::-1]
# print(string)

# Task 5b: reversing a string without using string slicing
# string = input("Enter a string: ")
# empty = ''
# for i in string:
#     empty =  i + empty 
#     print(empty)
# print(empty)


# Random number guessing program
# import random
# rannum = random.randint(1, 100) # generate a random number 1 - 100
# attempts = 0
# print(rannum)
# while attempts < 7:
#     guess = int(input('Guess a random number: '))
#     if guess < rannum:
#         print('Number is too small.')
#     elif guess > rannum:
#         print('Number is too big.')
#     else:
#         break
#     attempts += 1 
#     print(f"You have {7 - attempts} attempts left.")
# if guess == rannum:
#     print(f'{guess} is the correct number!')
# else:
#     print(f'you did not guess it, the correct number is {rannum}')
# elif attempts == 7:
#     print("No more tries.")

# play a game, where the player has 7 chances to guess the random number
#