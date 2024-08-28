'''
Task 2 
You have been asked to write a program that will create a password for a user. 
Open the file RM_SP.py 
You will see the following function that: 
Takes the name of the user 
Returns a text string of the name without the spaces 
'''

def removesp(text): 
    newtext = "" 
    for char in text: 
        if not char.isspace(): 
            newtext += char 
    return newtext 
'''
6. In your program, write a function changecase() that: 
Takes a single character as a parameter 
Returns the following: 
The lowercase letter of the character if the character is a uppercase alphabet 
The uppercase letter of the character if the character is a lowercase alphabet 
The character if the character is not an alphabet 
Save your program as CHGCASE_<your name>_<class>_<index_number>.py [3] 
'''
##### def function changecase()
# check if alphabet >>> isalpha()
# check if uppercase >>> isupper(), islower()
# change to lower/ upper case >> .lower(), .upper()
def changecase(char):
    if char.isalpha():
        if char.isupper():
            return char.lower()
        else:
            return char.upper()
    else:
        return char
x = changecase("1")
print(x)
'''
7. Extend the program by writing a function pwdgenerate() that: 
Takes the name of the user as a parameter 
Removes the spaces in the name using the removesp() function 
Creates a password by taking each alternate character in the name (without spaces) 
and changing the case of the character using changecase() function 
Appends a random digit of 0 to 9 inclusive at the end of the password 
Returns the generated password 

Sample Executions: 
>>> pwdgenerate(“John Tan”) 
‘jHtN2’ 

>>> pwdgenerate(“jOHN tAN”) 
‘JhTn9’ 

Save your program as PWDGEN_<your name>_<class>_<index_number>.py	[5] 
'''
# ALEXANDER >>>> A E A D R
import random
def pwdgenerate(name):
    newname = removesp(name) 
    newname = newname[::2] # find alternate
    tempstring = '' # holds a temporary string
    
    # loop through every character in newname
    for i in newname:    
        # change the current character to upper/ lower
        letter = changecase(i)
        print(f'value of letter {letter}')

        # join it back to tempstring
        tempstring = tempstring + letter
        print(f'value of tempstring {tempstring}')

    # generate a random number and it to tempstring
        
    tempstring += str(random.randint(0, 9))
    return tempstring
x = pwdgenerate("John Tan")
print(x)
        
'''
8. Save your program as PASSWD_<your name>_<class>_<index_number>.py 
Extend your program to create a user interface. The program must: 
Allow the user to input the name of the user with a suitable prompt message 
Loop until the user enters a valid name that has at least 5 characters with a suitable error message 
Generate and display the generated password of the user with a suitable message. 

Save your program [4] 
'''


##### STRING SLICING #######
# word = "SINGAPORE"
# var1 = word[0] ### letter S
# var2 = word[3] ### letter G

# # [start: stop: step]
# # SING
# var3 = word[:4]
# print(var3)

# var4 = word[::2] # take out alternate characters
# print(var4)
