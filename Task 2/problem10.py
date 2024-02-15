import random
pin_code = random.randint(1,100)
user_input = int(input("Guess The Number : "))
if user_input <= 0 or user_input >= 100:
    print("Please enter number between 1 to 100")
elif user_input == pin_code:
    print("Success Guessing Good Job")
else:
    print("Sorry Your Guessing Didn't Match ")
    print(f"Computer Generated this Number {pin_code}")