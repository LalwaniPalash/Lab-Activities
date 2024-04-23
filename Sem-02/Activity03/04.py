import time
import math

print("\nProgram to perfeorm Triginometric functions on an angle!\n")
time.sleep(2) 

def calculate_trigonometric_values(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    
    sine_value = math.sin(angle_in_radians)
    cosine_value = math.cos(angle_in_radians)
    tangent_value = math.tan(angle_in_radians)

    cosecant_value = 1 / sine_value if sine_value != 0 else float('inf')
    secant_value = 1 / cosine_value if cosine_value != 0 else float('inf')
    cotangent_value = 1 / tangent_value if tangent_value != 0 else float('inf')

    print(f"\nAngle: {angle_in_degrees} degrees")
    print(f"Sine: {sine_value}")
    print(f"Cosine: {cosine_value}")
    print(f"Tangent: {tangent_value}")
    print(f"Cosecant: {cosecant_value}")
    print(f"Secant: {secant_value}")
    print(f"Cotangent: {cotangent_value}\n")

try:
    angle_degrees = float(input("Enter an angle in degrees: "))
    calculate_trigonometric_values(angle_degrees)
except ValueError:
    print("Error: Invalid Input! Please enter a valid numerical value for the angle.")
