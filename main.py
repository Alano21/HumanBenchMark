import os
import time
from colorama import init, Fore, Style
from ReactionTime import ReactionTime
from NumberMemory import NumberMemory
from VerbalMemory import VerbalMemory
from GuessNumberGame import GuessNumberGame
from GuessWord import Hangman
from FindWrongWord import FindWrongWordGame

init(autoreset=True)

def display_scoreboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + Style.BRIGHT + "Scoreboard:")
    try:
        with open("scoreboard.txt", "r") as file:
            scores = file.readlines()
            if scores:
                for score in scores[-10:]:  
                    print(score.strip())
            else:
                print("No scores available.")
    except FileNotFoundError:
        print("Scoreboard file not found.")
    input(Fore.YELLOW + Style.BRIGHT + "\nPress ENTER to return to the main menu...")

def main():
    nickname = input(Fore.YELLOW + Style.BRIGHT + "Enter your nickname: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print(Fore.GREEN + Style.BRIGHT + "Welcome to the Brain Games!")
        print(Fore.CYAN + Style.BRIGHT + "1. Reaction Time")
        print(Fore.CYAN + Style.BRIGHT + "2. Number Memory")
        print(Fore.CYAN + Style.BRIGHT + "3. Verbal Memory")
        print(Fore.CYAN + Style.BRIGHT + "4. Guess Number Game")
        print(Fore.CYAN + Style.BRIGHT + "5. Hangman")
        print(Fore.CYAN + Style.BRIGHT + "6. Find Wrong Word")
        print(Fore.MAGENTA + Style.BRIGHT + "7. View Scoreboard")
        print(Fore.RED + Style.BRIGHT + "8. Exit")
        user_choice = int(input(Fore.YELLOW + Style.BRIGHT + "Choose game: "))

        os.system('cls' if os.name == 'nt' else 'clear') 

        if user_choice == 1:
            game = ReactionTime(nickname)
            game.play()
        elif user_choice == 2:
            game = NumberMemory(nickname)
            game.play()
        elif user_choice == 3:
            game = VerbalMemory(nickname)
            game.play()
        elif user_choice == 4:
            game = GuessNumberGame(nickname)
            game.play()
        elif user_choice == 5:
            game = Hangman(nickname)
            game.play()
        elif user_choice == 6:
            game = FindWrongWordGame(nickname)
            game.play()
        elif user_choice == 7:
            display_scoreboard()
        elif user_choice == 8:
            print(Fore.GREEN + Style.BRIGHT + "Exiting the game. Goodbye!")
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Please choose again.")
            continue

        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()