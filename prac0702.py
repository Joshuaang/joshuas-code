'''
# Question 1: Declare a function greet that takes a name as a parameter and returns a greeting message.
# Example input: name = 'John'
# Expected output: 'Hello, John!'
'''
# Write your code here
def greet(name):
    return 'Hello, ' + name + '!'
print(greet('John')) #this code will test your function

'''
# Question 2: Declare a function that takes two numbers as parameters and returns their sum.
# Example input: a = 5, b = 3
# Expected output: 8
'''
# Write your code here
def add(num1, num2):
    return num1 + num2
print(add(5, 3)) #this code will test your function

'''
# Question 3: Declare a function that takes a number as a parameter 
# and returns True if the number is even, otherwise False.
# Example input: number = 4
# Expected output: True
'''
# Write and test your code here
def even(num):
    if num % 2 == 0:
        return True
    else: 
        return False
print(even(5))

'''
# Question 4: Declare a function that takes a list of numbers 
as a parameter and returns the sum of the list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 15
'''
# Write and test your code here
def sumoflst(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
print(sumoflst([1, 2, 3, 4, 5]))

'''
# Question 5: Declare a function that takes a string as a parameter and returns the string in uppercase.
# Example input: text = 'hello'
# Expected output: 'HELLO'
'''
# Write and test your code here
def caps(text):
    return text.upper()
print(caps('hello'))

'''
# Question 6: Declare a function that takes a number as a
parameter and returns a string "positive" if the number is positive, 
"negative" if the number is negative, and "zero" if the number is zero.
# Example input: number = -1
# Expected output: 'negative'
'''
# Write and test your code here
def typeofnum(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'
print(typeofnum(0))

'''
# Question 7: Declare a function that takes two numbers as parameters and returns the larger number.
# Example input: a = 7, b = 10
# Expected output: 10
'''
# Write and test your code here
def larger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(larger(200, 100))

'''
# Question 8: Declare a function that takes a list of strings as a parameter
and returns the first longest string.
# Example input: strings = ['apple', 'banana', 'cherry']
# Expected output: 'banana'
'''
# Write and test your code here
def longest(lst):
    for i in lst:
        longest = 0
        longestword = ''
        if len(i) > longest:
            longest = len(i)
            longestword = i
    return longestword
print(longest(['apple', 'banana', 'cherry', 'watermelon']))

'''
# Question 9: Declare a function that takes a string and a number as parameters 
and returns the string repeated that many times.
# Example input: text = 'abc', count = 3
# Expected output: 'abcabcabc'
'''
# Write and test your code here
def repeat(string):
    return string * 3
print(repeat('abc'))    

'''
# Question 10: Declare a function that takes a list of numbers as a parameter 
and returns the average of the list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 3.0
'''
# Write and test your code here
def avg(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)
print(avg([1, 2, 3, 4, 5]))

'''
# Question 11: Declare a function that takes a string as a parameter and returns the string reversed.
# Example input: text = 'hello'
# Expected output: 'olleh'
'''
# Write and test your code here
def rev(text):
    return text[::-1]
print(rev('hello'))

# strings...
def rev2(text):
    # without using string slicing
    # loop 
    temp = ''
    for i in text:
        temp = i + temp
    return temp
print(rev2('watermelon'))

# list reverse without slicing
def rev3(text):
    # without using string slicing
    # loop 
    temp = []
    for i in text:
        temp.insert(0, i)
    return temp
print(rev3([1,2,3,4]))

'''
# Question 12: Declare a function that takes a list of numbers as a parameter and 
returns the smallest number.
# Example input: numbers = [3, 1, 4, 1, 5]
# Expected output: 1
'''
# Write and test your code here
def smallest(lst):
    smallest = max(lst) + 1 
    for i in lst:
        if i < smallest:
            
            smallest = i
    return smallest
print(smallest([3, 1, 4, 2, 5]))

'''
# Question 15: Declare a function that takes a list of numbers as a parameter and 
# returns a new list with each number squared.
# Example input: numbers = [1, 2, 3]
# Expected output: [1, 4, 9]
'''
# Write and test your code here
def squared(lst):
    sqlst = []
    for i in lst:
        sqlst.append(i ** 2)
    return sqlst
print(squared([1, 2, 3]))