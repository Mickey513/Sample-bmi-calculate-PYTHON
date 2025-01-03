# Program to calculate BMI and classify health status

# Ask the user to input their weight in kilograms
weight = input("Please enter your weight in kilograms: ")

# Validate if the input is a number
try:
    weight = float(weight)
except ValueError:
    print("Invalid input! Please enter a valid number for weight.")
    exit()

# Ask the user to input their height in meters
height = input("Please enter your height in meters: ")

# Validate if the input is a number
try:
    height = float(height)
except ValueError:
    print("Invalid input! Please enter a valid number for height.")
    exit()

# Calculate BMI using the formula BMI = weight / height^2
bmi = weight / (height * height)

# Classify BMI and display the result
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, and you are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}, and you are in the normal weight range.")
elif 25 <= bmi < 29.9:
    print(f"Your BMI is {bmi:.2f}, and you are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}, and you are obese.")
