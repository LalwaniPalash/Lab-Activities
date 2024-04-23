class TextAnalyzer:
    def count_words(self, text):
        words = text.split()
        return len(words)

    def count_characters(self, text):
        text_without_spaces = text.replace(" ", "")
        text_without_punctuation = ''.join(char for char in text_without_spaces if char.isalnum())
        return len(text_without_punctuation)

analyzer = TextAnalyzer()

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

word_count = analyzer.count_words(text)
print("Total words in the text:", word_count)

character_count = analyzer.count_characters(text)
print("Total characters in the text (excluding spaces and punctuation):", character_count)
