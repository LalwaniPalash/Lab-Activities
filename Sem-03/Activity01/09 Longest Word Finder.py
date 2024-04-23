import time

print("Program to Find Longest word in a Line!\n")
time.sleep(2)

def LongestWordFinder(line):
    punctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    MaxLength = 0
    noPunctuations = ""
    for char in line:
        if char not in punctuations:
            noPunctuations += char
    LongestWord = noPunctuations.split(" ")
    for i in LongestWord:
        if len(i) > MaxLength:
            MaxLength = len(i)
            LongestWord = i

    print(f"The longest word is ({LongestWord}) with length of ({MaxLength}) characters.")

line = None
while line is None:
    try:
        line = str(input("Enter a string: "))
    except ValueError:
        print("Please enter a valid line.")

LongestWordFinder(line)
