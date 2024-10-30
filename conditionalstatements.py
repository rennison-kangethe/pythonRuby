#python script that checks if a number is even or odd number
num=int(input("Enter a number: "))
if num%2 == 0:
     print(f"{num} is even number")
else:
    print(f"{num} is odd number")


#create a program that prints the largest of the three numbers
# Taking input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Using conditional statements to find the largest number
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")


