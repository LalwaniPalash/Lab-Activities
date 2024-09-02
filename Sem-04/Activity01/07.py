def to_fahrenheit(num):
    f = ((num * 9)/5) + 32
    return f

def fahrenheit(celcius):
    fahrenheit = []
    for i in celcius:
        fahrenheit.append(to_fahrenheit(i))
    return fahrenheit
    
celcius = [30, 40, 50, 60, 10]
fahrenheit = fahrenheit(celcius)

print(fahrenheit)
