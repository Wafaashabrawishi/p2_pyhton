#!/usr/bin/env python
import random
from colorama import *
# init()
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, thier_move):
        pass

    def my_learn(self, my_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class CyclerPlayer(Player):
    index = -1

    def move(self):
        self.index += 1
        if self.index == 3:
            self.index = 0
        return moves[self.index]


class HumanPlayer(Player):
    def move(self):
        asking = input('''What would like to throw \U0001F63B?''')
        while True:
            if asking in moves:
                return asking
            elif asking == "z":
                print(Fore.MAGENTA + '''
                Don't forget to play with us again\U0001F3B2''')
                quit()
            else:
                asking = input('''Enter a valid choice
What would like to throw or enter "z" to exit?''')


class RepeatPlayer(Player):
    pass


class ReflectPlayer(Player):
    index = 0

    def move(self):
        if self.index == 0:
            self.index += 1
            return random.choice(moves)
        return self.my_move

    def my_learn(self, my_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1   # human plalyer
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p2.my_learn(move1)

        print(f"\U0001F464Player 1: {move1}  \U0001F464Player 2: {move2}")
        if move1 == move2:
            print(Fore.YELLOW + '''       It's a tie \U0001F9D0 ''')
            print(Fore.CYAN + "     Do not be sad \U0001F63F")
            print(Fore.CYAN + " You still have a chance to win\U0001F4AA")
            print()
            print(Fore.BLUE + '''           Score \U0001F3C6''')
            print(Fore.YELLOW + '''
            \U0001F464Player 1 :''', self.p1.score, Fore.YELLOW + '''
            \U0001F464Player 2 :''', self.p2.score)

        elif beats(move1, move2):
            print(Fore.GREEN + '''      Player1 won \U0001F47B\U0001F389 !!''')
            print(Fore.RED + ''' Don't stop me now \U0001F46F,
            cause i'm having a good time \U0001F3B6''')
            print()
            print(Fore.BLUE + '''       Score \U0001F3C6''')
            self.p1.score += 1
            print(Fore.GREEN + '''
            \U0001F464Player 1 :''', self.p1.score, Fore.RED + '''
            \U0001F464Player 2 :''', self.p2.score)
        else:
            print(Fore.GREEN + '''      Player2 won \U0001F47B\U0001F389 !!''')
            print(Fore.RED + ''' Don't stop me now \U0001F46F,
            cause i'm having a good time\U0001F3B6''')
            print()
            print(Fore.BLUE + '''       Score \U0001F3C6''')
            self.p2.score += 1
            print(Fore.RED + '''
            \U0001F464Player 1 :''', self.p1.score, Fore.GREEN + '''
            \U0001F464Player 2 :''', self.p2.score)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print(Fore.BLUE)
        print('     Game start\U0001F929    ')
        print()
        round_num = int(input(Fore.CYAN + "How many rounds you want to play?"))
        for round in range(round_num):
            print(f"Round {round}:")
            self.play_round()
        print(Fore.MAGENTA + "GAME IS OVER \U0001F47E !!")


if __name__ == '__main__':
    print(Fore.MAGENTA + '''
    \U0001F57AWelcome to Rock Paper Scissor Game\U0001F57A''')
    print(Fore.YELLOW + '''        You can play either:
        "Rock\U0001F311"
        "Paper\U0001F4C4"
        "Scissors\U00002702"''')
    print(Fore.RED + '''If you want to exit, Enter "z"''')
    choice = input(Fore.BLUE + '''      Please Enter Your Selection:
        "Random"
        "Reflect"
        "Repeat"
        "Cycler"''')
    while True:
        if choice == "z":
            print(Fore.MAGENTA + '''
            Hope you enjoy it. See you next time \U0001F64B !!''')
            quit()
        elif choice == "random":
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
            break
        elif choice == "reflect":
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
            break
        elif choice == "repeat":
            game = Game(HumanPlayer(), Player())
            game.play_game()
            break
        elif choice == "cycler":
            game = Game(HumanPlayer(), CyclerPlayer())
            game.play_game()
            break
        else:
            print(Fore.RED+'''      \U0001F6D1 WARNINNG !!!!''')
            print(Fore.YELLOW + '''    This is not a valid choice''')
            print('''   So, who would you like to play with?''')
            print(Fore.BLUE + '''   Please enter your choice:
            "Random"
            "Reflect"
            "Repeat"
            "Cycler"''')
        choice = input()
