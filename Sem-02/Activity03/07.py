import time
import math

print("\nProgram to get obtain and print the values of three angles rounded to the next integer!\n")
time.sleep(2)

def calculate_angles(a, b, c):
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    
    A = round(A)
    B = round(B)
    C = round(C)

    return A, B, C

a = 5
b = 7
c = 8

angles = calculate_angles(a, b, c)
print(f"Angle A: {angles[0]} degrees")
print(f"Angle B: {angles[1]} degrees")
print(f"Angle C: {angles[2]} degrees")
