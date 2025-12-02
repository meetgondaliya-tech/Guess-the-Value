# Author: Meet Gondaliya
# Date: 02-12-2025 - Tuesday
# Project: Guess the Value 💰👥

import random

ra_value = random.randint(1, 100)
print("Random value generated! (Hidden from player)")

user_input = int(input("Enter your guess (1–100): "))

while user_input != ra_value:
    if user_input < ra_value:
        print("Too Low!!! 😒")
    else:
        print("Too High!!! 😊")

    user_input = int(input("Try again: "))

print("🎉 You Win! You guessed the right number!")
