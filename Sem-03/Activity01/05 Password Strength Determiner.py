print("Password Strength Determiner!\n")

def strengthDeterminer(line):
    print("Determining the Strength of your password...")

    upperCase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowerCase = set("abcdefghijklmnopqrstuvwxyz")
    specialChars = set("!@#$%^&*()_+-=[]{}|;:,.<>?")
    numbers = set("0123456789")
    strength = 0

    if len(line) >= 10:
        strength += 1
    if any(char in upperCase for char in line):
        strength += 1
    if any(char in lowerCase for char in line):
        strength += 1
    if any(char in specialChars for char in line):
        strength += 1
    if any(char in numbers for char in line):
        strength += 1

    return strength

def getRating(strength):
    if strength == 0:
        return "Very Poor"
    elif strength == 1:
        return "Poor"
    elif strength == 2:
        return "Average"
    elif strength == 3:
        return "Good"
    elif strength == 4:
    	return "Very Good"
    else:
        return "Excellent"

def suggestImprovements(line):
    suggestions = []
    if len(line) < 10:
        suggestions.append("Add more characters to make it longer.")
    if not any(char.isdigit() for char in line):
        suggestions.append("Include numbers.")
    if not any(char.isalpha() for char in line):
        suggestions.append("Include letters.")
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in line):
        suggestions.append("Include special characters.")

    return suggestions

line = None
while line is None:
    try:
        line = input("Enter a string: ")
    except ValueError:
        print("Please enter a valid line.")

strength = strengthDeterminer(line)
rating = getRating(strength)
print("Strength:", strength)
print("Rating:", rating)

if strength <= 3:
    suggestions = suggestImprovements(line)
    print("Suggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
