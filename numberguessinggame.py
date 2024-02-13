
import math

def number_guessing_game(lower_bound, upper_bound):
    winning_number = 20
    while True:
        guess_count = None
        user_guess = int(input("Enter your guess: "))
        if user_guess < winning_number:
            print("Too Low.")
        elif user_guess > winning_number:
            print("Too high.")
        else:
            print("You Win!!!")
            break
        
