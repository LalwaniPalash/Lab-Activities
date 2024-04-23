import time

print("Program to Find the most frequent word in a Line!\n")
time.sleep(2)

def MostFrequentWord(line):

    print("Removing Punctuations...")

    punctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    LineWithoutPunctuations = ""
    for char in line:
        if char not in punctuations:
            LineWithoutPunctuations += char
    print(f"This is the text without punctuations:\n {LineWithoutPunctuations}")

    print("Counting occurrence of each word...")

    words = {}
    for word in LineWithoutPunctuations.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    most_frequent_word = max(words, key=words.get)
    max_occurrences = words[most_frequent_word]

    print(f"The most frequent word is '{most_frequent_word}' with {max_occurrences} occurrences.")

line = None
while line is None:
    try:
        line = str(input("Enter a string: "))
    except ValueError:
        print("Please enter a valid line.")

MostFrequentWord(line)
