import random
def guess(number):
    random_number = random.randint(1, number)
    guess = True
    while guess:
        guess = int(input(f"Guess a number between 1 and {number}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low. ")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        else:
            print(f'Yay, congrats! You have guessed the number {random_number} correctly!')
            break;

guess(10)
