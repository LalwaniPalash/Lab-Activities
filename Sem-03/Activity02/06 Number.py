class Number:

	def setNumber(self, n):
		self.n = n

	def getNumber(self):
		return self.n

	def printNumber(self):
		print(self.n)

	def isNegative(self):
		if self.n < 0:
			print("The number is Negative.")
		else:
			print("The number is not Negative.")

	def isDivisibleBy(self, x):
		self.x = x
		if (self.n % self.x) == 0:
			print(f"The number {self.n} is divisible by {self.x}.")
		else:
			print(f"The number {self.n} is not divisible by {self.x}.")

	def absoluteValue(self):
		return abs(self.n)

n1 = Number()

n1.setNumber(10)
print(n1.getNumber())
n1.printNumber()
n1.isNegative()
n1.isDivisibleBy(5)
print(n1.absoluteValue())
