import time

print("Program to calculate Body-Mass Index!")
time.sleep(2)

w = None
h = None
while w is None: 
    try:
        w = float(input("Enter your weight in kg: "))
        h = float(input("Enter your height in meters: "))
    except ValueError: 
        print("Invalid Number!")

calculation = w / (h**2)
category = None

if calculation < 16.0:
    category = "Severely Underweight"
elif 16.0 <= calculation < 18.5:
    category = "Underweight"
elif 18.5 <= calculation < 25.0:
    category = "Normal"
elif 25.0 <= calculation < 30.0:
    category = "Overweight"
elif 30.0 <= calculation < 35.0:
    category = "Moderately Obese"
elif 35.0 <= calculation < 40.0:
    category = "Severely Obese"
else:
    category = "Morbidly Obese"

print(f"The BMI of a person with weight {w} kg and height {h} meters is {calculation:.1f} and belongs to the {category} category.\nThe data used for calculation was provided by WHO.")
