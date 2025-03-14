#Instructions:

#Basic Calculator Program Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.#

num1 = int(input("Enter your first number:"))
operator =(input("Enter your operator:"))

num2 = int(input("Enter your first number:"))



if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print (num1*num2)
elif operator =="/":
    print(num1/num2)
else:
    print("Invalid Operator")