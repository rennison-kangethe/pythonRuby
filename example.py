# Example: Recommend clothing based on weather
weather = input("Enter the weather (sunny, rainy, cloudy): ").lower()

if weather == "sunny":
    print("Wear sunglasses and a hat.")
elif weather == "rainy":
    print("Don't forget your umbrella.")
elif weather == "cloudy":
    print("It might rain, carry a jacket.")
else:
    print("Invalid weather input.")

# Example: Calculate discount based on purchase amount
amount = float(input("Enter the purchase amount: "))

if amount >= 1000:
    discount = 0.2  # 20%
elif amount >= 500:
    discount = 0.1  # 10%
else:
    discount = 0.05  # 5%

final_amount = amount - (amount * discount)
print(f"After applying discount, you need to pay: ${final_amount:.2f}")

# Example: Check the strength of a password
password = input("Enter your password: ")

if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong password.")
elif len(password) >= 6:
    print("Moderate password. Try adding more characters.")
else:
    print("Weak password. Consider using more characters and symbols.")

# Example: Calculate BMI and provide feedback
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are obese.")

# Example: Check if a person is eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
elif age > 0:
    print("You are not eligible to vote yet.")
else:
    print("Invalid age.")

# Example: Check username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Access granted.")
elif username == "admin":
    print("Incorrect password.")
else:
    print("Invalid username.")

# Example: Provide instructions based on traffic light color
light = input("Enter the traffic light color (red/yellow/green): ").lower()

if light == "red":
    print("Stop!")
elif light == "yellow":
    print("Prepare to stop.")
elif light == "green":
    print("Go!")
else:
    print("Invalid color. Please enter red, yellow, or green.")

