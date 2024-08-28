### EXAMPLE DICTIONARY
# A dictionary variable holds a key and value pair
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
# write and test your code here 
dictionary = {'hamburger':10, 'pizza':18.5, 'lasagne':25.70, 'fries':5}

'''
################ Retrieve values from a dictionary ###############
Print out the price of Lasagne only
Print out the price of Fries only
'''
# write and test your code here 
print(dictionary['lasagne'])
print(dictionary['fries'])

'''
########### Change the value of a dictionary key ###############
Change the price of hamburger to 20
Change the price of Fries to 3
'''
# write and test your code here 
dictionary['hamburger'] = 20
dictionary['fries'] = 3
print(dictionary)

'''
############ Increase the value of a dictionary key ############
Increase the price of Lasagne by 5
Decrease the price of Pizza by 3
'''
# write and test your code here 
dictionary['lasagne'] -= 5 
dictionary['pizza'] -= 3
print(dictionary)

'''
############### Add a new key/ Value to the dictionary #####################
Add a new menu item => Pasta which cost 15
Add a new menu item => Sandwich which cost 6
'''
# write and test your code here 
dictionary['pasta'] = 15 
dictionary['sandwich'] = 6
print(dictionary)

'''
############### Add a new key/ Value to the dictionary #####################
Delete menu item Pasta
'''
# write and test your code here 
del dictionary['pasta']
print(dictionary)

'''
########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of food item that you sell
# only display the keys
'''
# for i in dictionary:
#   print(i)
  
'''
########### Loop through to Retrieve Values ##################
Write a for loop, and only print out the price
'''
# write and test your code here 
# for i in dictionary:
#   print(dictionary[i])

'''
########### Loop through to Retrieve Key and Values ##################
Write a for loop, and print out the menu key and values
e.g.
Hamburger costs $10.00
Pizza costs $18.50
'''
# write and test your code here 
for i in dictionary:
  print(f'{i} costs ${dictionary[i]}')

'''
#################### Challenge 1 ######################################
Write a program to calculate how much money you need to buy all the items in the menu.
'''
# write and test your code here 
sum = 0
for food in dictionary:
  food_price = dictionary[food] # retrieves the prices
  sum = sum + food_price 
#print(sum)

'''
############### Challenge 2 ##########################################
Write a program to determine the most expensive item in the menu
'''
# write and test your code here 
highest = 0 
highestitem = ''
for f in dictionary:
  if dictionary[f] > highest:
    highest = dictionary[f]
    highestitem = f
#print(highestitem)

'''
################ Challenge 3 ########################################
#### Due to inflation, prices have increased. Update all the prices by 10%
'''
# write and test your code here 
for j in dictionary:
  dictionary[j] += dictionary[j] * (10/100)
  print(dictionary[j])
  
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

### CHALLENGE: implement a wallet feature, so you have limited money to buy the item
Keep asking until no more money to buy
'''
# write and test your code here 
name = input('Hello, what is your name? ')
wallet = 20
dictionary = {'hamburger':10, 'pizza':18.5, 'lasagne':25.70, 'fries':5}

# if "hamburger" in dictionary: # check if something exists in a variable (dictionary)
#     # this is exist

while True:
  for i in dictionary:
    order = input(f'Hi {name}, what would you like to eat? ')
    if order in dictionary:
      print(f'Great choice! Please pay {dictionary[i]}. Your order will be delivered soon!')
      wallet -= dictionary[i]
    elif order not in i:
      print(f"I'm sorry {name}, we don't sell {order}.")
  if order.lower() == 'exit':
    print('Ok, bye!')
  

'''
Q2
You are given a list of computing paper 1 marks and paper 2 marks

paper1 = {"Ken": 80, "Mike": 84, "Ash": 55, "Zee": 65}
paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

Design a program to

1a.  update Ken's computing mark to 83 for paper 1 
1b.  update Mike's computing mark to 58 for paper 2 

2.  show the average of paper 1 marks and average of paper 2 marks

3.  ask user to enter a person and the paper he wants to search. 
If the person is in the list, show the respective mark.
Otherwise shows that the person cannot be found
'''
