import random
import math

def play():
    user = input("whats your choice?... 'r' is for rocks 'p' is for papers 's' is for scissors: ")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:  # tie logic
        return (0, user, computer)

    # r>s, s>p, p>r
    def win(user, computer):   # win logic
        # returns true if the user beats the computer
        if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
            return True
        return False

    if win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)


def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary or computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print("you chose {} and computer chose {}.Its a TIE".format(user, computer))
        elif result == 1:
            player_wins +=1
            print("you chose {} and computer chose {}.But sorry YOU WON".format(user, computer))
        else:
            computer_wins +=1
            print("you chose {} and the computer chose {}. But sorry YOU LOST".format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print("You have won the best out of {}. what a champ..!!".format(n))
        print("CONGRATULATIONS!!!!!!")
    else:
        print("You have lost the best out of {}...Sorry better luck next time..".format(n))
        print("Well played...")


print(play_best_of(5))
