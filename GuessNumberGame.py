import random

class GuessNumberGame:
    def __init__(self, nickname):
        self.number_to_guess = random.randint(0, 100)
        self.attempts = 0
        self.guessed = False
        self.nickname = nickname

    def play(self):
        print("Welcome to the Guess Number Game!")
        print("I have selected a number between 0 and 100. Try to guess it!")

        while not self.guessed:
            try:
                user_guess = int(input("Enter your guess: "))
                self.attempts += 1

                if user_guess < self.number_to_guess:
                    print("Higher!")
                elif user_guess > self.number_to_guess:
                    print("Lower!")
                else:
                    self.guessed = True
                    print(f"Congratulations! You've guessed the number in {self.attempts} attempts.")
                    self.save_score()
            except ValueError:
                print("Please enter a valid number.")

    def save_score(self):
        with open("scoreboard.txt", "a") as file:
            file.write(f"{self.nickname} - GuessNumberGame - Attempts: {self.attempts}\n")

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    game = GuessNumberGame(nickname)
    game.play()