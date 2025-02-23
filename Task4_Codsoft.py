import random
def computer_choice():
    return random.choice(['rock','paper','scissors'])

def winner(user,computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return 1
    else:
        return 0
    
def game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock,paper,or scissors:").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice.Please choose rock, paper, scissors")
            continue
        computer = computer_choice()
        print("Computer Choose:",computer)

        result = winner(user_choice,computer)
        print(result)

        if result == 1:
            print("You win")
            user_score += 1
        elif result == 0:
            print("Computer wins")
            computer_score += 1
        
        print(f"You Score: {user_score} | Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no):").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
game()