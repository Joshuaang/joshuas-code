import math
'''
Challenge 6:
A programmer is writing a program to calculate the 
check digit for a 12-digit integer.

The check digit is calculated by multiplying the digits 
in odd positions by 3 and the digits in even positions by 1. 
These values are added together to produce a total. 
The total is subtracted from the next multiple of 10 to 
give a final value. If the final value is 10, the check digit is X.

Example: 
12-digit integer = 1  0  3  4  5  6  2  7  1  0  1  3
Result           = 3  0  9  4  15 6  6  7  3  0  3  3
Total = 3 + 0 + 9 + 4 + 15 + 6 + 6 +7 + 3 + 0 + 3 + 3 = 59
The next multiple of 10 is 60 (*hint: nextnum = math.ceil(num/10) * 10)
So, check digit = 60 - 59 = 1

(a) The The program code function calculate() takes a 
    12-digit number as a parameter. It calculates the 
    check digit and returns the check digit.

    Write the code for the function calculate [6]

(b) The main program:
•	Takes as input a 12-digit number until a valid 
    12-digit integer is entered
•	Calls the function calculate() with the valid input 
    as a parameter
•	Outputs the number with the check digit as its 13th digit

Write the code for the main program. [5]

Test that:
103456271013 = 1
123456789012 = 0
135792468013 = 5
'''
# import math
# def calculate(digits):
#     while True:
#         if len(digits) != 12:
#             print('digits must be 12') 
#             break
#         else:
#             odd = digits[0:-1:2]
#             even = digits[1::2]
#             total = 0
#             for o in odd:
#                 total = total + int(o)*3
#             for e in even:
#                 total = total + int(e)*1
#             nextnum = math.ceil(total/10) * 10
#             newnum = nextnum - total 
#             return newnum
# print(calculate('135792468013'))

'''
Challenge 7:
A developer needs to extract specific characters from a 
given string to generate a user ID.

(a) Write a function generate_user_id(name, birthdate) 
    that takes a user's full name as a single string in the 
    format "First Last" and a birthdate in the format "YYYYMMDD". 
    The function should return a user ID consisting of:

    - The first three letters of the last name (in uppercase),
    - The last two digits of the year of birth,
    - The first letter of the first name (in lowercase).
For example:
generate_user_id("John Doe", "19901225") should return DOE90j.
[6 marks]

(b) Write a main program that:

    - Takes as input a full name and birthdate,
    - Calls the generate_user_id() function,
    - Outputs the generated user ID.
Test cases:

generate_user_id("Alice Tan", "20030515") should return TAN03a.
generate_user_id("Michael Johnson", "19850911") should return JOH85m.
[4 marks]
'''
# def generate_user_id(name, birthdate):
#     id = ''
#     namesplit = name.split()
#     firstname = namesplit[0]
#     surname = namesplit[1]
#     birthdatelast2 = birthdate[2:4]
#     id = id + surname[0:3].upper() + birthdatelast2 + firstname[0].lower() 
#     return id
# print(generate_user_id("John Doe", "19901225"))
# print(generate_user_id("Alice Tan", "20030515"))
# print(generate_user_id("Michael Johnson", "19850911"))

'''
Challenge: Credit Card Validation
A financial institution needs to verify the validity of credit card numbers 
using the Luhn algorithm.

Task 1: Implementing the Luhn Algorithm
(a) Write a function is_valid_credit_card(card_number) that takes 
    a credit card number as a string and checks if it is valid according 
    to the Luhn algorithm. The function should:

    - Start from the rightmost digit (check digit) and move left.
    - Double every second digit. If the doubling results in a number greater 
      than 9, subtract 9 from it.
    - Sum all the digits (including those not doubled).

If the total sum is divisible by 10, return True 
(indicating the card number is valid); otherwise, return False.

Example:

is_valid_credit_card("4539148803436467") should return True.
is_valid_credit_card("1234567812345670") should return False.
[6 marks]

Task 2: Testing the Function
(b) Test your function with the following credit card numbers 
and determine if they are valid:

4539148803436467
1234567812345670
4485275742308327
6011514433546201
1234567812345678
Write the expected output for each test case.
'''
def is_valid_credit_card(card_number):
    total = 0
    if card_number.isalpha():
        print('Your card must be a digit')
    elif card_number.isdigit():
        cardsecond = card_number[1::2]
        for i in cardsecond:
            i = int(i) * 2
            if int(i) > 9:
                i -= 9
            else:
                pass
            total += int(i)
    if total % 10 == 0:
        return True
    elif total % 10 != 0:
        return False
print(is_valid_credit_card("4539148803436467"))
print(is_valid_credit_card("4485275742308327"))
print(is_valid_credit_card("6011514433546201"))
print(is_valid_credit_card("1234567812345678"))
