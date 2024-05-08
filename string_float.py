"""
Name: Garrett Helms
File: string_float.py
Date: May 2, 2024
Purpose: operate strings and number data types together in various ways.

"""
#01. prompt: ask for birthday
birthday = input("How old are you?")

#converts birthday to interger, adds 1
birthday_int = (int(birthday) + 1)

#prints value of birthday + 1 
next_birthday = print(f"Oh cool! so on your next birthday you'll be {str(birthday_int)} \n")

#02. prompt: asks for amount of egg cartons
egg_carton = input("How many egg cartons do you have?")

#multiplies egg cartons by 12 (eggs)
carton_mult = (int(egg_carton)*12)


#prints total eggs
carton_answer = print(f"So you have {str(carton_mult)} eggs! \n")

#03. prompt: asks for number of cookies
cookies = input("Okay, how many cookies do you have?")

#04. prompt: asks for number of people
people = input("And how many people are there?")


#converts both to int, divides cookies per person
cookies_div = (int(cookies) / int(people))

#prints answer 
cookies_per_person = print(f"Congrats! you have {str(cookies_div)} cookies per person!")



