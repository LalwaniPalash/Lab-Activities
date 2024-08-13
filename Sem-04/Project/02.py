def guess_number(low, high):
    while low <= high:
        mid = (low + high) // 2
        guess = input(f"Is {mid} your number? (Enter 'h' if the number is higher, 'l' if it's lower, and 'c' if I guessed correctly): ").strip().lower()
        
        if guess == 'c':
            print("Game over. I guessed the number correctly.")
            return
        elif guess == 'h':
            low = mid + 1
        elif guess == 'l':
            high = mid - 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
    
    print("It seems there was an issue. Please make sure your number is within the specified range.")

print("Think of a number between 1 and 100.")
guess_number(1, 100)
