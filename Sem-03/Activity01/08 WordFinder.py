def searchWord(word, wordList):
    positions = []
    for i, w in enumerate(wordList):
        if w.lower() == word.lower():
            positions.append(i)
    return positions

def main():
    wordList = ["apple", "banana", "orange", "grape", "banana", "kiwi", "apple"]

    searchWordInput = input("What word would you like to search for?\n- ")

    positions = searchWord(searchWordInput, wordList)

    print(positions)

main()
