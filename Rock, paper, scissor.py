import random

def get_user_choice():
    user_choice = input("Choose one: rock, paper, or scissors: ")
    user_choice = user_choice.lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose one: rock, paper, or scissors: ")
        user_choice = user_choice.lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to rock, paper, scissors!")
    print('')
    while True:
        print("-------------------")
        print('')
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print('')
        print(f"You chose: {user_choice}")
        print('')
        print(f"Computer chose: {computer_choice}")
        print('')
        print(determine_winner(user_choice, computer_choice))
        print('')
        play_again = input("Do you want to play again? (yes/no): ")
        print('')
        play_again = play_again.lower()
        if play_again != 'yes':
            print("Goodbye!")
            break
play_game()