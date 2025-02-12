import random
import os
import time

class VerbalMemory:
    def __init__(self, nickname):
        self.seen_words = set()
        self.score = 0
        self.lives = 3
        self.word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
        self.nickname = nickname

    def play(self):
        while self.lives > 0:
            word = self.get_new_word()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Lives: {self.lives}")
            user_input = input(f"Is the word '{word}' new or seen? (new/seen): ").strip().lower()

            if user_input not in ["new", "seen"]:
                print("Invalid input! Please enter 'new' or 'seen'.")
                time.sleep(2)
                continue

            if user_input == "new":
                if word in self.seen_words:
                    self.lives -= 1
                    print(f"Wrong! You have {self.lives} lives left.\n")
                else:
                    self.seen_words.add(word)
                    self.score += 1
                    print(f"Correct! Your score is {self.score}.\n")
            elif user_input == "seen":
                if word in self.seen_words:
                    self.score += 1
                    print(f"Correct! Your score is {self.score}.\n")
                else:
                    self.lives -= 1
                    print(f"Wrong! You have {self.lives} lives left.\n")

        print(f"Game over! Your final score is {self.score}.")
        self.save_score()

    def get_new_word(self):
        return random.choice(self.word_list)

    def save_score(self):
        with open("scoreboard.txt", "a") as file:
            file.write(f"{self.nickname} - VerbalMemory - Final score: {self.score}\n")

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    game = VerbalMemory(nickname)
    game.play()