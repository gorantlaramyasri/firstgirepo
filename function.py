# # Create a function:-
# def greet():
#     print('Good Mornig.!')
#     # Call a function
# greet()
# greet()
# greet()
# greet()
# # 1 predefinde functions:--
# #  len()
# #  type()
# #  int()
# #  str()
# #  print()
# #  list()

# predefined functions:--
#  len()
#  type()
#  int()
#  str()
#  print()
#  list()

# user defined function:--
# num1 = int(input('Enter a num1:'))
# num2 = int(input('Enter a num2:'))
# def addition (a, b):
#     print(a + b)
# addition(num1 , num2)    

# num1  = int(input('Enter a num1:'))
# def square (a):
#     print(a ** 2)
# square(num1)    
    
# num1 = int(input('enter a num1:'))
# def mod_of_num1 (a):
#        print(a % 2)
# # mod_of_num1(num1)       

# num1 = int(input('Enter a num1:'))
# num2 = int(input('Enter a num2:'))
# def normal_and_floor_div(a, b):
#     print(a /b)
#     print(a // b)

# normal_and_floor_div(num1, num2)
   
# num1 = int(input('Enter a num1:'))
# num2 = int(input('Enter a num2:'))
# def maximin_num(a, b):
#     if a > b:
#       print(a)

#     else:
#        print(b)
# maximin_num(num1, num2)       

# num1 = int(input('Enter a num1:'))
# num2 = int(input('Enter a num2:'))
# def minimun_num(a, b):
#     print(a if a < b else b)
# minimun_num(num1, num2)    

# str1 = input('Python')
# len(str1)
# def reverse 
#        print(a)
# reverse(str1)    

# num1 = int(input('Enter a num1:'))
# num2 = int(input('Enter a num2:'))
# range = range(0, 20)
# def even_of_num1_and_num2(a, b):
#     print(a % 2 ==0)
# even_of_num1_and_num2(num1, num2)    


# start  = int(input('Enter a num1:'))
# stop= int(input('Enter a num2:'))
# def even_of_range(a, b):
#     for i in range(a, b):
#           if i % 2 == 0:
#                print(i)
# even_of_range(start, stop)

# str1 = input('enter a str')
# vowels= ['a', 'e', 'i', 'o', 'u']
# def find_vowels(a):
#         for char in (a):
#                 if char in vowels:
#                     print(char)
# find_vowels(str1) 
# ###############day 2 #####3333
# difference between return and print


# def greet():
#     print('Good mornig:')
# greet()

# def greet1():
#     return('Good afternoon')
# greet1()  
# print(greet1()) 
# def divide(c, d):
#     return c / d                  
# print(divide(15, 4))
        
# def is_even_num(num):
#     if num % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')
# is_even_num(12)                

# def is_greeter_num(num):
#     if num > 50:
#         return 'Greeter'
#     else:
#         return 'Lesser'
# print(is_greeter_num(33))       
               
############# Arguments  ################
# def datatype (data):
#     print(type(data))    

# def which_greater(a, b, c):

# def odd_num(num1, num2):
#     if num1 % 2 == 0 and num2 % 2 == 0:
#         print(f"{num1} and {num2} are even")
#     elif num1 % 2 ==0 and num2 % 2== 0 :
#        print(f"{num2} is even")
#     else:
#         print(f"{num1} and {num2} are odd")
# odd_num(num2=23, num1=3)           

# DEfault arguments  ####====
# def greetme(me='ramya'):
#     print(f"hello {me}")
# greetme()
# greetme('eshu')    


# def find_nums_divisible_by_5(start =0, end = 50):
#     for i in range(start, end):
#         if i % 5 == 0:
#             print(i)
#         else:
#             pass
# find_nums_divisible_by_5(10, 20)            

# ++++++++++++++++++++Variable length arguments++++++++++++++++++++++++++++++++
# def sum_of_nums(a, b):
#     print(a + b)
# sum_of_nums(34, 3)    

# def sum_of_nums(*args):
#     print(sum(args))
# sum_of_nums(12, 2, 10, 23, 23, 5, 7)

# def greater_even_num(*args):
#     list_of_even = []
#     for i in args:
#         if i % 2 == 0:
#            list_of_even.append(i)
#         else:
#             pass
#     print(max(list_of_even))       
# greater_even_num(23, 2, 45, 67, 90)           

# def divisible_by_3_5 (a, b):
#     if a & b / 3 & 5:
#         print()

# def lowest_num_divisible_by_5(*args):
#     list_of_nums = []
#     for i in args:
#         if i % 3 == 0 and i % 5 == 0:
#             print()      

# def greater_string(*args):
#     dict1 = {}
#     for i in args:
#         dict1[i] = len(i)
#     list_keys = list(dict1.keys())
#     list_values = list(dict1.values())

#     high_value = max(list_values)
#     index_value = list_values.index(high_value)
#     print(dict1)
#     print(list_keys)
#     print(list_values)
#     print (max(list_values))
# greater_string('ravi', 'ramya', 'rajeshwari', ) 