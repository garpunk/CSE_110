'''
Name: Garrett Helms
File: meal_price.py
Date: May 8th, 2024

Purpose: computing the price of a meal


'''

child_meal_price = float

adult_meal_price = float

children = int

adults = int

sales_tax = float

child_meal_total = float(child_meal_price) * int(children)

adult_meal_total = float(adult_meal_price) * int(adults)

meal_subtotal = child_meal_total * adult_meal_total

meal_tax = meal_subtotal * (sales_tax / 100)

meal_total = meal_subtotal + meal_tax

meal_subtotal_ans = print(f"{str(meal_subtotal)}")

meal_total_ans = print(f"{str(meal_total)}")

payment = float

payment_change = meal_total - payment





