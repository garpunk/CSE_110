
'''
Name: Garrett Helms
File: teach_activity_3.py
Date: May 6th, 2024

Purpose: compute the area of different shapes.


'''


# Import math Library
import math

#01 prompt: input:ask user for length of square
square_area = input("What is the length of a side of the square?")

#calculate the side squared using float data type
sq_area_calc = float(square_area)**2

#print the output: convert calculation to string
sq_area_ans = print(f" \n The area of the square is: {str(sq_area_calc)} \n")

#02 prompt: ask user for length of a rectangle
rect_length = input("What is the length of rectangle?")

#03 prompt: ask user for width of rectangle
rect_width = input("What is the width of the rectangle?")

#multiply length x width to get rectangle area
rect_area = float(rect_length) * float(rect_width)

#print the output: convert calculation to string
rect_area_ans = print(f" \n The area of the rectangle is: {str(rect_area)} \n")

#04 prompt: ask user for the radius of a circle
circle_rad = input("What is the radius of the circle?")

#using formula area = pi * radius^2, calculate the area using function from math module
circle_area = math.pi*(float(circle_rad)**2) #= 3.14*(radius^2)

#print the output: convert calculation to string
circle_area_ans = print(f"\n The area of the circle is: {str(circle_area)} \n") 

#stretch activity: getting user to put in a single input for multiple outputs

#05 prompt: asks user for a single value
omni_number = input(""" Okay, lets try a challenge.
                    
                    Give me a single number to represent:
                        
                    1. a squares side
                    2. a circles radius
                    3. a cubes edge
                    4. a spheres radius   
                    
                    and I'll take this number to calculate:
                    
                    1. the squares area
                    2. the circles area
                    3. the cubes volume
                    4. the circles volume  
                    
                    the number:    """)

#calculate square area for users number
omni_num_square = float(omni_number)**2

#calculate circle area for users number
omni_num_circle = math.pi*(float(omni_number)**2)

#calculate cube volume from users number
omni_num_cube = float(omni_number)**3

#calculate sphere volume from users number
omni_num_sphere = (4/3)*math.pi*(float(omni_number)**3)


#prints all calculation values in an easy-to-read format:
omni_num_ans = print(f""" \n Okay, here are the results:
                     
                     1. the squares area: {str(omni_num_square)}  
                     2. the circles area: {str(omni_num_circle)}  
                     3. the cubes volume: {str(omni_num_cube)} 
                     4. the spheres volume: {str(omni_num_sphere)}  """)


#06 prompt: input:ask user for length of square(centimeters)
square_area_cent = input("What is the length of a side of the square(cm)?")

#calculate the side squared using float data type(centimeters)
sq_area_calc_cent = float(square_area)**2

#calculate in meters from centimeters
sq_area_calc_met = sq_area_calc_cent / 10000



#print the output: convert calculation to string
sq_area_cent_ans = print(f" \n The area of the square in centimeters is: {str(sq_area_calc_cent)}cm^2 \n")

#print the output: convert calculation to string
sq_area_met_ans = print(f" \n The area of the square in meters is: {str(sq_area_calc_met)}m^2 \n")

#07 prompt: ask user for length of a rectangle(centimeters)
rect_length_cent = input("What is the length of rectangle(cm)?")

#08 prompt: ask user for width of rectangle(centimeters)
rect_width_cent = input("What is the width of the rectangle(cm)?")

#multiply length x width to get rectangle area in centimeters
rect_area_cent = float(rect_length_cent) * float(rect_width_cent)

#calculate in meters (from centimeters)
rect_area_met = rect_area_cent / 10000

#print the output: convert calculation to string
rect_area_cent_ans = print(f" \n The area of the rectangle is: {str(rect_area_cent)}cm^2 \n")

#print the output: convert calculation to string
rect_area_met_ans = print(f" \n The area of the square in meters is: {str(rect_area_met)}m^2 \n")


#09 prompt: ask user for the radius of a circle(centimeters)
circle_rad_cent = input("What is the radius of the circle(cm)?")

#using formula area = pi * radius^2, calculate the area using function from math module in centimeters
circle_area_cent = math.pi*(float(circle_rad)**2)

#calculate in meters (from centimeters)
circle_area_met = circle_area_cent / 10000

#print the output: convert calculation to string
circle_area_cent_ans = print(f"\n The area of the circle is: {str(circle_area_cent)}cm^2 \n") 

#print the output: convert calculation to string
circle_area_met_ans = print(f"\n The area of the circle is: {str(circle_area_met)}m^2 \n") 



#testing git commit function for repository
