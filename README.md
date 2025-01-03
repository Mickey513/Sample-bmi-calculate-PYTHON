# BMI Calculator Program

This is a simple Python program that calculates the Body Mass Index (BMI) based on the user's input for weight and height, then classifies their health status according to the calculated BMI.

## Features

- Prompts the user to input their weight (in kilograms).
- Prompts the user to input their height (in meters).
- Validates the input to ensure the user enters valid numbers.
- Calculates the BMI using the formula: `BMI = weight / height^2`.
- Classifies the user based on their BMI into one of the following categories:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 <= BMI < 24.9
  - Overweight: 25 <= BMI < 29.9
  - Obese: BMI >= 30

## How to Run the Program

1. Ensure you have **Python** installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).
   
2. Save the code to a file, e.g., `bmi_calculator.py`.

3. Open your terminal or command prompt.

4. Navigate to the folder where `bmi_calculator.py` is saved.

5. Run the program by typing:
   ```bash
   python bmi_calculator.py


  // Example Output //
python

Please enter your weight in kilograms: 70
Please enter your height in meters: 1.75
Your BMI is 22.86, and you are in the normal weight range.
