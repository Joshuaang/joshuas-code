import prac0628
'''
Open the file DONATIONS.ipynb

Save the file as

This task is to edit program code so that donations for different types
of beneficiary organisations (e.g. Children, Elderly, Disabled, Religious)
can be added to a dictionary.

The following program has a dictionary that contains the different
types of beneficiary organisations and the donations they have received.

The program allows the user to :
input  whether they want to add a donation record to the dictionary
'''

# donations = {'Children': 1200,
#              'Elderly': 1000,
#              'Disabled': 800,
#              'Religious':2000
#             }
# add = input("Would you like to add a donation record? (Y or N): ")

'''
For each of the sub-tasks, add a comment using the hash symbol "#" at
the beginning of your code to indicate the sub-task that the program code belongs to.
For Example:
# Task 1.1
Program Code

For all sub-tasks, you can assume that all user input is valid.
'''

'''
##############  Task 1.1 ##############
Edit the program so that if the user enters the value 'Y' for add, the program:
- Allows the user to input the type of benedificiary organisation they want to donate to
- Allows the user to input the amount they want to donate
- Adds the type of beneficiary organisation and the donation amount to the dictionary
  in the format "beneficiary organisation": amount
- Outputs the dictionary at the end of the program

Save your program [3]
'''
#write your code here
# donations = {'Children': 1200,
#              'Elderly': 1000,
#              'Disabled': 800,
#              'Religious':2000
#             }
# add = input("Would you like to add a donation record? (Y or N): ")

# if add.upper() == 'Y':
#     # do something to handle
#     org = input("Enter type of organisation? Options are Children, Elderly, Disabled, Religious : ")

#     # check for existence of the key
#     if org in donations:
#         amt = int(input("Enter the amount to donate: "))
#         donations[org] = donations[org] + amt
#     else:
#         print('Invalid Organisation type, please try again')
    
# elif add.upper() == 'N':
#     print('Ok thank you bye bye')
# else:
#     print('Invalid option, pls try again')
    
# print(donations)
'''
############## Task 1.2##############
Copy and paste your program from sub-task 1.1
Edit the program to check that the donation is at least $10
and in multiples of $10.

Otherwise, the program should inform the user about the input requirements
and ask the user to re-enter the information

Save your program [3]
'''
#write your code here
# donations = {'Children': 1200,
#              'Elderly': 1000,
#              'Disabled': 800,
#              'Religious':2000
#             }
# add = input("Would you like to add a donation record? (Y or N): ")

# if add.upper() == 'Y':
#     # do something to handle
#     org = input("Enter type of organisation? Options are Children, Elderly, Disabled, Religious : ")

#     # check for existence of the key
#     if org in donations:
        
#         while True:
#             amt = int(input("Enter the amount to donate: "))
#             if amt >= 10 and amt % 10 == 0:
#                 donations[org] = donations[org] + amt
#                 print("thank you for your donation")
#                 break 
#             else:
#                 print("You must donate at least $10 and in multiples of $10")    
#     else:
#         print('Invalid Organisation type, please try again')
    
# elif add.upper() == 'N':
#     print('Ok thank you bye bye')
# else:
#     print('Invalid option, pls try again')
    
# print(donations)

'''
############### Task 1.3 ##############
Copy and paste your program from sub-task 1.2

Edit the program to display the type of beneficiary organisation that received the highest donation
and the amount received. A suitable output message must be used.

Save your program [3]
'''
#write your code here
# donations = {'Children': 1200,
#              'Elderly': 1000,
#              'Disabled': 800,
#              'Religious':2000
#             }
# add = input("Would you like to add a donation record? (Y or N): ")

# if add.upper() == 'Y':
#     # do something to handle
#     org = input("Enter type of organisation? Options are Children, Elderly, Disabled, Religious : ")

#     # check for existence of the key
#     if org in donations:
        
#         while True:
#             amt = int(input("Enter the amount to donate: "))
#             if amt >= 10 and amt % 10 == 0:
#                 donations[org] = donations[org] + amt
#                 print("thank you for your donation")
#                 break 
#             else:
#                 print("You must donate at least $10 and in multiples of $10")    
#     else:
#         print('Invalid Organisation type, please try again')
    
# elif add.upper() == 'N':
#     print('Ok thank you bye bye')
# else:
#     print('Invalid option, pls try again')

# # code to find org with highest donation
# highestdonation = 0
# highesttype = ''
# for thisorg in donations:
#     if donations[thisorg] > highestdonation:
#         highestdonation = donations[thisorg] # find the highest donation value
#         highesttype = thisorg
# print(f'{highesttype} has the highest donation amount of ${highestdonation}')
# #print(donations)

'''
############## Task 1.4 ##############
Copy and paste your program from sub-task 1.3

Edit the program to find the total amount donated across all the types of beneficiary
organisation. A suitable output message must be used.

Save your JupyterLab notebook for Task 1    [1]

'''
#write your code here

# donations = {'Children': 1200,
#              'Elderly': 1000,
#              'Disabled': 800,
#              'Religious':2000
#             }
# add = input("Would you like to add a donation record? (Y or N): ")

# if add.upper() == 'Y':
#     # do something to handle
#     org = input("Enter type of organisation? Options are Children, Elderly, Disabled, Religious : ")

#     # check for existence of the key
#     if org in donations:
        
#         while True:
#             amt = int(input("Enter the amount to donate: "))
#             if amt >= 10 and amt % 10 == 0:
#                 donations[org] = donations[org] + amt
#                 print("thank you for your donation")
#                 break 
#             else:
#                 print("You must donate at least $10 and in multiples of $10")    
#     else:
#         print('Invalid Organisation type, please try again')
    
# elif add.upper() == 'N':
#     print('Ok thank you bye bye')
# else:
#     print('Invalid option, pls try again')

# # code to find org with highest donation
# highestdonation = 0
# highesttype = ''
# total = 0
# for thisorg in donations:
#     total = total + donations[thisorg]
#     if donations[thisorg] > highestdonation:
#         highestdonation = donations[thisorg] # find the highest donation value
#         highesttype = thisorg
# print(f'{highesttype} has the highest donation amount of ${highestdonation}')
# print(f'The total amount of donations is ${total}')
#print(donations)