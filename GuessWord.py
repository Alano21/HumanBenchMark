import random
import os

class Hangman:
    def __init__(self, nickname):
        self.word = random.choice(["python", "java", "kotlin", "javascript"])
        self.correct_letters = set(self.word)
        self.guessed_letters = set()
        self.attempts = 6
        self.nickname = nickname

    def display_word(self):
        display = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(display)

    def play(self):
        print("Welcome to Hangman!")
        while self.attempts > 0 and self.correct_letters != self.guessed_letters:
            self.display_word()
            guess = input("Guess a letter or the full word: ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')  
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("You already guessed that letter.")
                elif guess in self.correct_letters:
                    self.guessed_letters.add(guess)
                    print("Good guess!")
                else:
                    self.guessed_letters.add(guess)
                    self.attempts -= 1
                    print(f"Wrong guess. You have {self.attempts} attempts left.")
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess == self.word:
                    self.guessed_letters = self.correct_letters
                    break
                else:
                    self.attempts -= 1
                    print(f"Wrong guess. You have {self.attempts} attempts left.")
            else:
                print("Please enter a single letter or the full word.")

        if self.correct_letters == self.guessed_letters:
            print(f"Congratulations! You guessed the word: {self.word}")
            self.save_score("Win")
        else:
            print(f"Game over! The word was: {self.word}")
            self.save_score("Lose")

    def save_score(self, result):
        with open("scoreboard.txt", "a") as file:
            file.write(f"{self.nickname} - Hangman - Result: {result}, Word: {self.word}, Attempts left: {self.attempts}\n")

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    game = Hangman(nickname)
    game.play()