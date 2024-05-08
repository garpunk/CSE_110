'''
Name: Garrett Helms
File: meal_price.py
Date: May 8th, 2024

Purpose: computing the price of a meal


'''
#01. prompt Ask the user for the price of a child meal
child_meal_price = input("What is the price of a child's meal?")

#02. prompt Ask the user for the price of an adult meal
adult_meal_price = input(" \n What is the price of an adult's meal?")

#03. prompt Ask the user for the price of drinks
drinks_price = input(" \n What is the price of drinks?")

#04. prompt Asker user for price of dessert
dessert_price = input(" \n What is the price of dessert?")


#04. prompt Ask the user for the number of children 
children = input(" \n How many children are there?")

#05. prompt Ask the user for the number of adults
adults = input(" \n How many adults are there?")

#06. prompt Ask the user for number of drinks purchased
drinks = input(" \n How many drinks would you like to order?")

# prompt Ask the user for the number of desserts purchased
desserts = input(" \n How many desserts would you like to order?")

#07. prompt Ask the user for the sales tax rate 
sales_tax = input(" \n What is the sales tax rate(%)?")

# calculate child meal total
child_meal_total = float(child_meal_price) * int(children)

# calculate adult meal total
adult_meal_total = float(adult_meal_price) * int(adults)

# calculate drink total
drinks_total = float(drinks_price) * int(drinks)

# calculate dessert total
dessert_total = float(dessert_price) * int(desserts)

# calculate meal subtotal
meal_subtotal = float(child_meal_total) + float(adult_meal_total) + float(drinks_total) + float(dessert_total)

#round meal subtotal
meal_subtotal_round = format(meal_subtotal, ".2f")

#round the sales tax
sales_tax_round = format(float(sales_tax), ".2f")

# calculate meal tax
meal_tax = float(meal_subtotal_round) * (float(sales_tax_round) / 100)

# round meal tax to nearest 2 decimals
meal_tax_round = format(meal_tax, ".2f")

# calculate meal total
meal_total = float(meal_subtotal_round) + float(meal_tax_round)

# round meal total to nearest 2 decimal places
meal_total_round = format(meal_total, ".2f")

# display meal subtotal
meal_subtotal_ans = print(f"Subtotal: ${str(meal_subtotal_round)}")

# display meal tax
meal_tax_ans = print(f"Sales Tax: ${str(meal_tax_round)}")

# display meal total
meal_total_ans = print(f"Total: ${str(meal_total_round)}")

#08. prompt Ask user for payment amount
payment = input(" \n What is the payment amount?")

# calculate payment 
payment_change = float(payment) - float(meal_total)

# round change to 2 decimal places
payment_change_round = format(payment_change, ".2f")

# display user change
payment_change_ans = print(f" \n Change: ${str(payment_change_round)}")







