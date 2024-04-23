import time

print("Program to convert numbers to text!")
time.sleep(2)

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number = int(input("\nEnter a number: "))

num_str = str(number)

text_representations = ""

for digit in num_str:
    digit = int(digit)  
    text_representations += digits[digit] + " "  

text_representations = text_representations.strip()

print(f"\n{number} in text is: {text_representations}")
