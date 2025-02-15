"""
#age#
year_of_birth= int(input("Enter year of birth"))
current_year=2024
age=current_year-year_of_birth
print(f" You are {age} years old.")
"""

'''
#sum and product#
num1=float(input("Enter first number."))
num2=float(input("Enter second number."))
product=num1*num2
sum=num1+num2
print(f"The product is {product} and sum is {sum}")
'''
'''
N=float(input("Enter number N"))
print(f"The number {N}")
square=N**2
print(f"The value of its square is {square}")
'''
'''
#sum and product of two numbers#
num1=float(input("Enter number:"))
num2=float(input("Enter another number:"))
sum=num1 + num2
product=num1*num2
print(f"The sum is {sum} and the product is {product}")
'''
"""
#length and perimeter#
L=float(input('Enter the length of the rectangle:'))
B=float(input('Enter the breadth of the rectangle:'))
area=L*B
perimeter=2*(L+B)
print(f"The area of the rectangle is {area} and perimeter is {perimeter}")
"""
'''
radius=float(input("Enter radius:"))
diameter=radius*2
print(f"The diameter is {diameter}")
circumference=3.141*diameter
print(f"The circumference is {circumference}")
area=3.14*radius**2
print(f"The area is {area}")
'''
'''
height=float(input('enter the height of the triangle:'))
base=float(input("Enter the base of the triangle:"))
area=height*1/2*base
print(f"The area of the triangle is {area}")
'''
'''
price=float(input('Enter the price:'))
VAT_RATE=0.15
VAT_DUE=price*VAT_RATE
price_with_VAT=price+VAT_DUE
print(f"The VAT due is{VAT_DUE:2f}")
print(f"the VAT price is {price_with_VAT:2f}")
'''
'''
#area of right angled triangle#
a=float(input("Enter the opposite length:"))
b=float(input("Enter the adjascent length:"))
hypotnuse=a*2+b*2
print(f"The hypotnuse is {hypotnuse}")
'''

'''
initial_value=float(input("Enter the initial reading:"))
final_value=float(input("Enter the final reading:"))
consumption=final_value-initial_value
unit_cost=1.50
final_cost=consumption*unit_cost
print(f"The cost of consumption is {final_cost}")
'''

'''
Initial_km=float(input("Enter the initial kilometers of the car:"))
Final_km=float(input("Enter final kilometers of the car"))
Fuel=float(input("Enter fuel used."))
Distance=Final_km-Initial_km
Fuel_consumption=Distance/Fuel
print(Fuel_consumption)
'''

'''
#force of gravitational attraction#
M1=float(input("Enter the first mass in kilograms:"))
M2=float(input("Enter the secodn mass in kilograms:"))
R=float(input("Enter the distance between the two planets"))
formula=((6.7*10**-11*M1*M2)/R**2)
print(f"The force is {formula}")
'''


population=43.0e6
growth_rate=0.123
for year in range(1,4):
    population*=(1+growth_rate)
    print(f"Year{year}:{population/1e6:.2f}millions")


'''
#midpoint#
x_coordinate1=float(input("Enter the first x-coordinate:"))
x_coordinate2=float(input("Enter the second x-coordinate:"))
y_coordinate1=float(input("Enter the first y-coordinate:"))
y_coordinate2=float(input("Enter the second y-coordinate:"))
mid_pointx=(0.5*(x_coordinate1+x_coordinate2))
mid_pointy=(0.5*(y_coordinate1+y_coordinate2))
print(f"The midpoint is {mid_pointx},{mid_pointy}")
'''
'''
import math #to input formula you use a math library#
x=5
numerator=(x**4-x**3+x**2-x)
denomenator=(x+1)**2-math.sqrt(x)
N=numerator/denomenator
print(f"N is {N}")
'''

'''
X=float(input("Enter the original mark:"))
A=float(input("Enter the original total:"))
B=float(input("Enter the new total:"))
proportion=X/A
converted_mark=X/A*B
print(f"the converted mark is {converted_mark}")
'''

import math
def solve_quadratic(a,b,c):







