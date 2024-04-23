import time

print("Palindrome Checker!\n")
time.sleep(2)

def PalindromeChecker(word):
	reversed_word = word[::-1]
	if word == reversed_word:
		print(f"The word ({word}) is a Palindrome.")
	else:
		print(f"The word ({word}) is not a Palindrome.")

word = input("Enter a word: ")
PalindromeChecker(word)
