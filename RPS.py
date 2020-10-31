import random
import fileinput
import sys


class Score:
    def __init__(self, player):
        score = 0
        self.player = player
        self.score = score
        with open('rating.txt', 'r+') as game:
            for line in game:
                if self.player in line:
                    break
            else:
                game.write(self.player + " " + str(self.score) + "\n")


class Rating:
    def __init__(self, player):
        self.player = player
        with open("rating.txt", 'r') as rating:
            for line in rating:
                if self.player in line:
                    line = line.rstrip()
                    ratings = line.split(" ")
                    # print(ratings)
                    self.score = int(ratings[1])
                    print("Your rating: " + (ratings[1]))
                    break


class ScoreUpdate:
    def __init__(self, player, score_change):
        self.player = player
        self.change = score_change
        with open("rating.txt", 'r+') as score_update:
            for line in score_update:
                if self.player in line:
                    line = line.rstrip()
                    score = line.split(" ")
                    self.score = int(score[1]) + int(self.change)
                    new = self.player + " " + str(self.score) + "\n"
                    break
        for line in fileinput.input('rating.txt', inplace=True):
            if line.strip().startswith(self.player):
                line = new
            sys.stdout.write(line)
            fileinput.close()


class Game:
    def __init__(self):
        self.player = str(input('Enter your name: '))
        list_of_options = input() or 'rock,paper,scissors'
        self.moves = list_of_options.split(",")
        self.game_lose = {'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
                          'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
                          'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
                          'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
                          'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
                          'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
                          'air': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
                          'paper': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
                          'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
                          'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
                          'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
                          'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
                          'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
                          'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
                          'fire': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock']}
        print('Hello, ' + self.player)
        Score(self.player)
        print("Okay, let's start")
        while True:
            self.computer_move = random.choice(self.moves)
            user_play = input().lower()
            if user_play == self.computer_move:
                print(f"There is a draw ({self.computer_move})")
                ScoreUpdate(self.player, 50)
            elif user_play == "!rating":
                Rating(self.player)
            elif user_play == "!exit":
                print("Bye!")
                break
            elif user_play not in self.moves:
                print("Invalid input")
            elif self.computer_move in self.game_lose[user_play]:
                print(f"Sorry, but the computer chose {self.computer_move}")
            else:
                print(f"Well done. The computer chose {self.computer_move} and failed")
                ScoreUpdate(self.player, 100)


Game()
