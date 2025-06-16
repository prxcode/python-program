# We all know first program is always Hello World
'''

-> print("Hello World")

 
 '''
# This is a simple Calculator program in python
# It can add, subtract, multiply and divide two numbers

print("Simple Calculator")
x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))
print("1 for Add")
print("2 for Sub")
print("3 for mul")
print("4 for div")
choice = int(input("Select Operations: "))

if choice == 1:
	print("Sum of",x,"and",y,"is: ",x+y)
elif choice == 2:
	print("Subtraction of",x,"and",y,"is: ",x-y)
elif choice == 3:
	print("Multiplication of",x,"and",y,"is: ",x*y)

elif choice == 4:
	print("Division of",x,"and",y,"is: ",x/y)
else: 
	print("Invalid Input")

