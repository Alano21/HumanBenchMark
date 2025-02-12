import random
import os
import time

class FindWrongWordGame:
    def __init__(self, nickname):
        self.level = 1
        self.score = 0
        self.nickname = nickname

    def introduce_typo(self, word):
        if len(word) > 1:
            index = random.randint(0, len(word) - 1)
            typo_word = word[:index] + random.choice('abcdefghijklmnopqrstuvwxyz') + word[index + 1:]
            return typo_word
        return word

    def generate_words(self):
        words = ["apple", "banana", "orange", "grape", "peach", "melon", "berry", "kiwi", "plum", "pear"]
        random.shuffle(words)
        typo_indices = random.sample(range(len(words)), self.level)
        for i in typo_indices:
            words[i] = self.introduce_typo(words[i])
        return words, typo_indices

    def play(self):
        while True:
            words, typo_indices = self.generate_words()
            print(f"Level {self.level}:")
            for i, word in enumerate(words):
                print(f"{i + 1}. {word}")
            user_input = input("Enter the numbers of the misspelled words separated by spaces: ")
            user_indices = list(map(int, user_input.split()))
            user_indices = [i - 1 for i in user_indices]
            if set(user_indices) == set(typo_indices):
                self.score += 1
                print("Correct! Moving to the next level.")
                self.level += 1
                time.sleep(1)  
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Incorrect. Game over.")
                break
        self.save_score()

    def save_score(self):
        with open("scoreboard.txt", "a") as f:
            f.write(f"{self.nickname} - FindWrongWord - Score: {self.score}\n")
        print(f"Your final score is {self.score}")

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    game = FindWrongWordGame(nickname)
    game.play()