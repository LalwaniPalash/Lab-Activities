name = input("Enter your name: ")

roll = None
while roll is None:
    try:
        roll = int(input("Enter your Roll Number: "))
    except ValueError:
        print("Roll Number should be an integer!")

if len(str(roll)) == 2:
    roll = "230100" + str(roll)
else:
    None

print(name)
print(roll)
