import time
import random

class ReactionTime:
    def __init__(self, nickname):
        self.reaction_time = 0
        self.nickname = nickname

    def play(self):
        print("Welcome to Reaction Time!")
        print("Instructions will appear shortly to press the ENTER key.")
        print("Your task is to press ENTER as quickly as possible after the prompt appears.")
        input("Press ENTER to start...")
        wait_time = random.uniform(1, 4)

        time.sleep(wait_time)

        print("Press NOW!")

        start_time = time.time()
        input()
        end_time = time.time()
        self.reaction_time = end_time - start_time
        print(f"Your reaction time is: {self.reaction_time:.3f} seconds")

        self.save_score()

    def save_score(self):
        with open("scoreboard.txt", "a") as file:
            file.write(f"{self.nickname} - ReactionTime - Reaction time: {self.reaction_time:.3f} seconds\n")

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    game = ReactionTime(nickname)
    game.play()