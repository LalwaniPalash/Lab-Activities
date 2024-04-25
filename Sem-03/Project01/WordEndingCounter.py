class WordEndingCounter:
    def __init__(self, text):
        self.text = text

    def count_s(self):
        words = self.text.split()
        count_s = 0
        for i in words:
        	if i.endswith("s"):
        		count_s+=1
        return count_s

    def count_es(self):
        words = self.text.split()
        count_es = 0
        for i in words:
        	if i.endswith("es"):
        		count_es+=1
        return count_es

    def count_ing(self):
        words = self.text.split()
        count_ing = 0
        for i in words:
        	if i.endswith("ing"):
        		count_ing+=1
        return count_ing

text = "This is a test string"
counter = WordEndingCounter(text)
print("Occurrences of words ending with 's':", counter.count_s())
print("Occurrences of words ending with 'es':", counter.count_es())
print("Occurrences of words ending with 'ing':", counter.count_ing())
