'''
The following program allows the weights of 15 bags of rice to be input. 
The correct weight for each bag of rice must be 
between 4.9 kg and 5.1 kg inclusive.
'''
# bags_rice = 15
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")
'''
Open the file RICEBAGS.py
Save the file as MYBAGS_<your name>_<center number>_<index number>.py

1.	Edit the program so that it:
a.	Accepts the weights for only 10 bags of rice.
[1]
'''
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# if bags_rice > 10 or bags_rice < 10:
#     print('Only 10 bags of rice is accepted')
# else:
#     for count in range(bags_rice):
#         bag_weight = float(input("Enter the weight of the bag of rice "))
#         if bag_weight > upper_bound:
#             print("The bag of rice is overweight")
#         if bag_weight < lower_bound:
#             print("The bag of rice is underweight")
        
'''
b.	Prints out the message “The bag of rice is the correct weight” 
when a weight entered is between 4.9kg and 5.1 kg inclusive.
[2]
'''
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     elif bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#     elif lower_bound <= bag_weight <= upper_bound:
#         print('The bag of rice is the correct weight')
        
'''
c.	Prints out the number of bags of rice that were underweight, 
as well as the number that were overweight, after the weights of 
all the bags have been entered.
[5]
'''
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# overweight = 0
# underweight = 0
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#         overweight += 1
#     elif bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#         underweight += 1
#     elif lower_bound <= bag_weight <= upper_bound:
#         print('The bag of rice is the correct weight')
# print(f'{overweight} bags of rice are overweight\n{underweight} bags of rice are underweight')

'''
Save your program.
2.	Save your program as VARBAGS_<your name>_<center number>_<index number>.py
Edit your program so that it works for any number of bags of rice.
Save your program.
[2]
'''
# bags_rice = int(input('Enter number of bags of rice: '))
# upper_bound = 5.1
# lower_bound = 4.9
# overweight = 0
# underweight = 0
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#         overweight += 1
#     elif bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#         underweight += 1
#     elif lower_bound <= bag_weight <= upper_bound:
#         print('The bag of rice is the correct weight')
# print(f'{overweight} bags of rice are overweight\n{underweight} bags of rice are underweight')

## open the file cyberattacks.txt
# count the number of vowels in the file
# how any a, e , i o, u
# output the answer to a file called vowelcount.txt

# a = 0
# e = 0
# i = 0
# o = 0 
# u = 0
# with open('cyberattacks.txt') as c:
#     contents = c.read()
#     for char in contents:
#         if char.lower() == 'a':
#             a += 1
#         elif char.lower() == 'e':
#             e += 1
#         elif char.lower() == 'i':
#             i += 1
#         elif char.lower() == 'o':
#             o += 1
#         elif char.lower() == 'u':
#             u += 1
# # print(a,e,i,o,u)
# print(f'A: {a}, E:{e}, I:{i}, O:{o}, U:{u}')