# please make sure you import this file from main.py so you can run this file.
# import practice_dict ## in main.py
### EXAMPLE DICTIONARY
example = {
  'key1': 'value1',
  'key2': 'value2',
  'key3': 'value3',
  'key4': 'value4'
}

'''
################ Define a dictionary ###############
Define a dictionary named menu which will store a food item and price of food

'hamburger' costs 10
'pizza' costs 18.5
'lasagne' costs 25.70
'fries' costs 5
'''
# write your code here 
menu = {'hamburger':10, 'pizza':18.5, 'lasagne':25.70, 'fries':5}

'''
################ Retrieve values from a dictionary ###############
Print out the price of Lasagne only
Print out the price of Fries only
'''
# write your code here 
print(menu['lasagne'])
print(menu['fries'])

'''
########### Change the value of a dictionary key ###############
Change the price of hamburger to 20
Change the price of Fries to 3
'''
# write your code here 
menu['hamburger'] = 20
menu['fries'] = 3
print(menu)

'''
############ Increase the value of a dictionary key ############
Increase the price of Lasagne by 5
Decrease the price of Pizza by 3
'''
# write your code here 
menu['lasagne'] += 5
menu['pizza'] += 3
print(menu)

'''
############### Add a new key/ Value to the dictionary #####################
Add a new menu item => Pasta which cost 15
Add a new menu item => Sandwich which cost 6
'''
# write your code here 
menu['pasta'] = 15
menu['sandwich'] = 6
print(menu)

'''
############### Add a new key/ Value to the dictionary #####################
Delete menu item Pasta
'''
# write your code here 
del menu['pasta']
print(menu)

'''
########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of food item that you sell
# only display the keys
'''
# write your code here 
for i in menu:
  print(i)

'''
########### Loop through to Retrieve Values ##################
Write a for loop, and only print out the price
'''
# write your code here 
for i in menu:
  print(menu[i])
  
'''
########### Loop through to Retrieve Key and Values ##################
Write a for loop, and print out the menu key and values
e.g.
Hamburger costs $10.00
Pizza costs $18.50
'''
# write your code here 
for i in menu:
  print(f'{i} costs {menu[i]}')

'''
#################### Challenge 1 ######################################
Write a program to calculate how much money you need to buy all the items in the menu.
'''
# write your code here
total = 0
for i in menu:
  total += menu[i]
print(total)

'''
############### Challenge 2 ##########################################
Write a program to determine the most expensive item in the menu
'''
# write your code here
highest = 0
highestkey = ''
for i in menu:
  if menu[i] > highest:
    highest = menu[i]
    highestkey = i
print(highestkey)

'''
################ Challenge 3 ########################################
#### Due to inflation, prices have increased. Update all the prices by 10%
'''
# write your code here 
for i in menu:
  menu[i] = menu[i] * 110/100
  print(menu[i])
  
'''
################ Challenge 4 ########################################
Upgrade this system where you ask customers what they want, and display the price 
# you can check if a key exists in a dicionaty, by using the 'in' keyword
# for example: if 'hamburger' in menu: will return true if hamburger exists 

Example:

Hello, What is your name? John
>>> Hi John, what would you like to eat? Laksa
>>> I'm sorry John, we don't sell Laksa. 

Hi John, what would you like to eat? Hamburger
>>> Great choice! Please pay $10.00. Your order will be delivered soon!
Hi John, what would you like to eat? Exit

Ok, bye!
'''
# write your code here 
name = input('What is your name? ')
while True:
  choice = input(f'Hi {name}, what would you like to eat? ')
  if choice == 'Exit':
    print("Ok, bye!")
    break
  elif choice not in menu:
    print(f"Im sorry {name}, we don't sell {choice}")
  elif choice in menu:
    print(f'Great choice! Please pay {menu[choice]}')
    



