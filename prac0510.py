import task2_2021
'''
Create a Password Validator program that checks if a password is strong.
1. Ask the user to input a password.
2. Check if the password is at least 8 characters long.
3. Check if it contains at least one uppercase letter and one lowercase letter
4. Check if it contains one digit.
5. Check if it contains a special character "!@#$%^&*()"
6. Provide feedback on which criteria the password pass/ or fail.
7. Indicate if the password is strong if all criteria are met.

'''
# checklen = False
# checkupper = False
# checklower = False
# checkdigit = False
# checkspec = False
# specialchar = "!@#$%^&*()"
# password = input("Enter a password: ")
# if len(password) == 8:
#     checklen = True
# for i in password:
#     if i.isupper():
#         checkupper = True
#     if i.islower():
#         checklower = True
#     if i.isdigit():
#         checkdigit = True
#     if i in specialchar:
#         checkspec = True
# if checklen and checkupper and checklower and checkdigit and checkspec == True:
#     print("Password accepted!")
# else:
#     print("Password rejected.")