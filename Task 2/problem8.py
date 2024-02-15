import random
import string
length = 8
characters = string.ascii_letters+ string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated Password:", password)
while True:
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        print(f"{number} is a numeric value")
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")