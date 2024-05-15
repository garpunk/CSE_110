'''
Name: Garrett Helms
File: physics_equation.py
Date: May 13th 2024
Purpose: running a physics equation to determine how fast an object will fall 

'''

#import math library
import math

#introduce user to the program
problem = print("This program will determine how fast an object will fall." +
                 " Please insert your values in the input's below")

#prompt user for mass in kg
mass = input(" \n What is the mass in kg?")

#prompt user for accelleration due to gravity in m/s^2
gravity = input(" \n What is the accelleration due to gravity in m/s^2? ")

#prompt user for time in seconds
time = input(" \n What is the time in seconds?")

#prompt user for density of fluid
density_fluid = input(" \n What is the density of fluid in kg/m^3?")

#prompt user for cross sectional area of projecticel in square meters
cross_sect_area = input(" \n What is the cross sectional area of the projectile in m^2?")

#prompt user for drag constant
drag_const = input(" \n What is the drag constant?")

#calculate cross sectional area
cross_sect_calc = (1/2) * float(density_fluid) * float(cross_sect_area) * float(drag_const)

#calculate the first part of the equation (v(t) = sqrt(mg/c))
vel_at_t_1 = math.sqrt(float(mass) * float(gravity) / cross_sect_calc)

#calculate the second part of the equation (1 - exp((-sqrt(mgc)/m)*t)
vel_at_t_2 = 1 - math.exp((-math.sqrt(float(mass) * float(gravity) * float(cross_sect_calc)) / float(mass)) * float(time))

#combine the two parts (v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)*t))
vel_at_t_calc = float(vel_at_t_1) * float(vel_at_t_2)

#calculate the terminal velocity
v_terminal = math.sqrt(float(mass) * float(gravity) / float(cross_sect_area))




#display the inner value of c 
cross_sect_ans = print(f" \n answer for inner value c is {(cross_sect_calc):.3f}")

#display the velocity at meters per second
vel_at_t_ans = print(f" \n velocity is {(vel_at_t_calc):.3f} m/s")

#display terminal velocity
v_terminal_ans = print(f" \n the terminal velocity is {v_terminal} m/s")



