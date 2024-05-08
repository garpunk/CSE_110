'''
Name: Garrett Helms
File: id_badge.py
Date: April 29th 2024
purpose: creating a program to prompt for name badge details and then outputting those details
'''

#general welcome text explaining what the user must do
welcome_text = print("Hi! welcome to badge creator! \n" +
                      "please fill out the prompts below to create your new name badge!")

#gather input from users
first_name = input("First Name: ")
last_name = input("Last Name: ")
email_addr = input("Email Address: ")
phone_num = input("Phone Number: ")
job_title = input("Job Title: ")
id_num = input("ID Number: ")
hair_col = input("Hair Color: ")
eye_col = input("Eye Color: ")
month_start = input("Month Started: ")
training = input("Have you completed monthly training? answer yes or no: ")




#print the input in a proper format according to badge requirements
print("Congratulations! Here is your new ID card \n \n" + "----------------------------------------")
print(f"{last_name.upper()}, {first_name}")
print(job_title.capitalize())
print(id_num + "\n \n")
print(email_addr.lower())
print(f"{phone_num} \n")
print(f"Hair Color: {hair_col.title()}\t \t Eye Color: {eye_col.title()}")
print(f"Month Started: {month_start.title()}\t \t Training: {training.title()}")
print("----------------------------------------")