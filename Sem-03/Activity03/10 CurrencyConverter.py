class CurrencyConverter:
    def __init__(self):
        self.exchangeRates = {"USD": 1.0, "EUR": 0.9}

    def convert(self, amount, fromCurrency, toCurrency):
        if fromCurrency in self.exchangeRates and toCurrency in self.exchangeRates:
            rateFrom = self.exchangeRates[fromCurrency]
            rateTo = self.exchangeRates[toCurrency]
            convertedAmount = amount * (rateTo / rateFrom)
            return convertedAmount
        else:
            print("Invalid currency provided. We only have USD and EUR.")
            return None


converter = CurrencyConverter()

amount = 100
fromCurrency = "USD"
toCurrency = "EUR"
convertedAmount = converter.convert(amount, fromCurrency, toCurrency)
print(f"{amount} {fromCurrency} is equal to {convertedAmount:.2f} {toCurrency}")
