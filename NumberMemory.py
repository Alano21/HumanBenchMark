import random
import time
import os

class NumberMemory:
    def __init__(self, nickname):
        self.level = 1
        self.nickname = nickname

    def generate_number(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(self.level)])

    def play(self):
        print("Welcome to Number Memory!")
        while True:
            number = self.generate_number()
            print(f"Remember this number: {number}")
            time.sleep(1 + (self.level - 1) * 0.2) 
            os.system('cls' if os.name == 'nt' else 'clear')
            user_input = input("Enter the number: ")
            if user_input == number:
                print("Correct! Moving to the next level.")
                self.level += 1
            else:
                print(f"Incorrect. The number was: {number}")
                self.save_score()
                break

    def save_score(self):
        with open("scoreboard.txt", "a") as file:
            file.write(f"{self.nickname} - NumberMemory - Level reached: {self.level}\n")
        print(f"Your final score is {self.level}")

if __name__ == "__main__":
    nickname = input("Enter your nickname: ")
    game = NumberMemory(nickname)
    game.play()