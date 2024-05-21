'''
Author: Garrett Helms
File: l5checkpoint.py
Date: May 20th 2024

purpose: else if elif  practice yeah


'''


first_num = input("What is the first number?") 
second_num = input("What is the second number?") 
if first_num > second_num:             
   print("The first number is greater")
else:
   print("The second number is greater")

if first_num != second_num:
   print("The numbers are not equal")
elif first_num == second_num:
   print("The numbers are equal")



fav_animal = input("What is your favorite animal?")

if fav_animal.lower() == "platypus":
   print("that's my favorite animal too!")
elif fav_animal.lower() == "bear":
   print("I love bears!")
else:
   print("That's not my favorite animal")

