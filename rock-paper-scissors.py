#!/usr/bin/env python3
import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.next_move = random_throw()

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random_throw()


class HumanPlayer(Player):
    def move(self):
        while True:
            move_choice = input("Rock, paper, or scissors?\n")
            for n in range(3):
                if moves[n] in move_choice:
                    return moves[n]
            print("Sorry, I didn't quite understand that.")


class ReflectPlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        for n in range(3):
            if my_move == moves[n]:
                self.next_move = moves[(n + 1) % 3]


class ConfidentPlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        success = beats(my_move, their_move)
        if success is True:
            return my_move
        if success is False:
            moves = ['rock', 'paper', 'scissors']
            moves.remove(my_move)
            moves.remove(their_move)
            self.next_move = moves[0]  # returns a move not used last round
            moves = ['rock', 'paper', 'scissors']  # resets the list


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def random_throw():
    return random.choice(['rock', 'paper', 'scissors'])


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("Tie!")
        else:
            result = beats(move1, move2)
            return result

    def play_game(self):
        print("Game start! Best 3 out of 5!")
        score1 = 0
        score2 = 0
        round = 1
        while score1 < 3 and score2 < 3:
            print(f"Round {round}:")
            success = self.play_round()
            if success is True:
                print("Player 1 wins!")
                score1 += 1
            elif success is False:
                print("Player 2 wins!")
                score2 += 1
            round += 1
        print("Game over!")
        if score1 == 3:
            print("Player 1 wins the game!")
        if score2 == 3:
            print("Player 2 wins the game!")
        print("Final score:\n" + f"Player 1: {score1}  Player 2: {score2}")


if __name__ == '__main__':
    CompPlayer = (RandomPlayer, ReflectPlayer, CyclePlayer, ConfidentPlayer)
    Opponent = random.choice(CompPlayer)
    game = Game(HumanPlayer(), Opponent())
    game.play_game()
