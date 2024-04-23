print("A Simple Word Replacement Program!\n")

def replaceWord(input_string, old_word, new_word):
    replaced_string = input_string.replace(old_word, new_word)
    return replaced_string

def replaceWordManual(input_string, old_word, new_word):
    words = input_string.split()
    for i in range(len(words)):
        if words[i] == old_word:
            words[i] = new_word
    replaced_string = ' '.join(words)
    return replaced_string

input_string = input("Enter a string: ")

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

replaced_string = replaceWord(input_string, old_word, new_word)
print("\nUsing in-built function:")
print("Replaced string:", replaced_string)

replaced_string_manual = replaceWordManual(input_string, old_word, new_word)
print("\nManual replacement (without in-built function):")
print("Replaced string:", replaced_string_manual)
