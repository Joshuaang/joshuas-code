# Pre ####
# Generate a list of 100 random numbers
# each number is a range from 1 to 1000 every number in this list must be unique
 
# import random
# numlist = [] # empty list
# while len(numlist) < 100:
#     rannum = random.randint(1,1000)
#     if rannum not in numlist:
#         numlist.append(rannum)
# print(numlist)

# # Find the smallest number in this list
# smallest = 1001
# for i in numlist:
#     if i < smallest:
#         smallest = i
# print(smallest)

# # Find the maximum number in this list
# biggest = 0
# for i in numlist:
#     if i > biggest:
#         biggest = i
# print(biggest)

# # Find the average of this list
# sum = 0
# for i in numlist:
#     sum += i
# print(sum/len(numlist))

'''
Mock Question 1 (Task 2) 

The following program allows the entry of temperatures for a week. 
The program checks if the temperature is within a normal range (24°C to 28°C inclusive). 

days = 7
normal_min = 24 
normal_max = 28 
for day in range(days): 
    temp = float(input("Enter the temperature for the day: ")) 
    if temp > normal_max: 
        print("The temperature is too high") 
    if temp < normal_min: 
        print("The temperature is too low") 
    if temp >= normal_min and temp <= normal_max:
        print("The temperature is normal")

Open the file TEMPERATURE.py 
Save the file as MYTEMP_<your name><center number><index number>.py 

Edit the program so that it: 
Q1: Accepts temperatures for only 5 days.  
[1 mark] 

Q2: Prints "The temperature is normal" when the temperature is between 24°C and 28°C inclusive.  
[2 marks] 

Q3: Counts and prints the number of days with temperatures too high and too low 
after all inputs.  
[4 marks] 

Save your program. 

Save your program as VARTEMP_<your name><center number><index number>.py 
Q4: Edit your program so that it works for any number of days. 
Save your program.  
[3 marks] 
'''
#Question 1 and Question 2 and Question 3
# days = 5
# normal_min = 24 
# normal_max = 28 
# maxcount = 0
# mincount = 0
# for day in range(days): 
#     temp = float(input("Enter the temperature for the day: ")) 
#     if temp > normal_max: 
#         print("The temperature is too high") 
#         maxcount += 1
#     if temp < normal_min: 
#         print("The temperature is too low") 
#         mincount += 1
#     if temp >= normal_min and temp <= normal_max:
#         print("The temperature is normal")
# print("Sorry! No more temperatures can be accepted.")
# print(f"Number of high temperature days: {maxcount}\nNumber of low temperature days: {mincount}")

#Question 4
# days = int(input("Enter number of days: "))
# normal_min = 24 
# normal_max = 28 
# maxcount = 0
# mincount = 0
# for day in range(days): 
#     temp = float(input("Enter the temperature for the day: ")) 
#     if temp > normal_max: 
#         print("The temperature is too high") 
#         maxcount += 1
#     if temp < normal_min: 
#         print("The temperature is too low") 
#         mincount += 1
#     if temp >= normal_min and temp <= normal_max:
#         print("The temperature is normal")
# print("Sorry! No more temperatures can be accepted.")
# print(f"Number of high temperature days: {maxcount}\nNumber of low temperature days: {mincount}")

'''
The following program generates an email ID for a user. 
It creates the email ID by taking the first three letters of the user’s first name 
nd appending it to the user's last name. It then verifies the user's email address. 

Program Code: 

firstname = input("Please enter your first name: ") 
lastname = input("Please enter your last name: ") 
email_id = firstname[:3] + lastname + "@example.com" 
print("Your email ID is " + email_id) 
email = input("Please enter your email address: ") 


Q1: Edit the program to ensure that the email ID is created using the 
first letter of the first name and the entire last name.  
[1 mark] 

Q2: The program needs to verify that the email address provided by the user is valid. 
Edit the program to: 
 Check if the email contains the '@' symbol. 
 Output a suitable error message if the email does not contain the '@' symbol, 
 and prompt the user to enter a valid email address repeatedly until 
 the correct format is provided. 
[4 marks] 


Q3: Edit the program to: 
Ask the user to re-enter their email address. 
Check that the second entry of the email address matches the first entry. 
Output the message "Your email address has been confirmed." if the email entries match. 
Otherwise, output the message "Email addresses do not match. Please re-enter your email address: " and read the email address again, repeating this until the entries match. 

[5 marks] 
'''
#Question 1
# firstname = input("Please enter your first name: ") 
# lastname = input("Please enter your last name: ") 
# email_id = firstname[0] + lastname + "@example.com" 
# print("Your email ID is " + email_id) 

#Question 2
# while True:
#     email = input("Please enter your email address: ") 
#     if '@' not in email:
#         print("Please add an @ in your email.")
#     else:
#         print(f'{email} is valid.')
#         break

#Question 3
# while True:
#     email = input("Please enter your email address: ") 
#     if '@' not in email:
#         print("Please add an @ in your email.")
#     else:
#         print(f'{email} is valid.')
#         break
# while True:
#     email2 = input("Re-Enter your email addrerss: ")
#     if email != email2:
#         retry = input(("Email addresses do not match. Please re-enter your email address: "))
#     else:
#         print("The entries match")
#         break
