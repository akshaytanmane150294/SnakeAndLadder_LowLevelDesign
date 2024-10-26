
from dice import Dice
from level import Level
from board import Board
from ladder import Ladder
from snake import Snake
from player import Player


class Game:
    def __init__(self):
        self.players = []
        self.dice = Dice(6)

        # let players select a level
        self.level = Level()
        self.select_level()

        # set up board
        self.board = Board(self.level.get_board_size())
        self.create_board()

    def select_level(self):
        level1 = Level('Easy', 30)
        level2 = Level('Medium', 50)
        level3 = Level('Hard', 100)

        selected_level = input('select level:Easy/Medium/Hard: ')
        if selected_level == 'Easy':
            self.level = level1
        elif selected_level == 'Medium':
            self.level = level2
        else:
            self.level = level3

    def create_board(self):
        ladders = {3: 22, 5: 8, 11: 26, 10: 98, 20: 29}
        snakes = {17: 4, 19: 7, 21: 9, 39: 3, 50: 25, 75: 19, 27: 1, 99: 10}
        for x, y in ladders.items():
            self.board.place_ladder(Ladder(x, y))

        for x, y in snakes.items():
            self.board.place_snake(Snake(x, y))

    def add_players(self):
        print("Add Players for a New Game")
        player_count = int(input("Enter Number of Players:"))
        for num in range(player_count):
            username = input(f"Enter name Player#{num+1}:")
            player_obj = Player(username)
            self.players.append(player_obj)

    def show_players(self):
        print(f'{len(self.players)} Players:')
        for player in self.players:
            print(player.username)

    def start_game(self):
        CONTINUE = True
        print("Starting Game....")
        round_number = 0
        while CONTINUE:
            round_number += 1
            print(f"==============={round_number}===============")
            for player in self.players:
                print(f'------> {player.username} turn')
                input("Throw dice ------> <Press Enter>")

                # Geneare Random Number b/w 1 and 6
                dice = self.dice.get_value()
                print(f'You got ----> {dice}')
                six_count = 0
                sum = dice
                while dice == 6:
                    input(f'Got {dice}, Throw again -----> <press Enter>')
                    dice = self.dice.get_value()
                    print(f'You got -----> {dice}')
                    six_count += 1
                    sum += dice
                    if six_count == 2:
                        print(" Wow! Consecutive 3 times 'Six'")
                        break
                pos = player.position + sum
                if self.board.is_snake_present(pos):
                    print(" Hiss!!! snake Bites ---> Snake ne Gand mar liya ")
                    dest = self.board.get_snake_tail(pos)
                    print(f'you fall down to {dest}')
                    player.position = dest
                elif self.board.is_ladder_present(pos):
                    print(" Great!! you Found a ladder ----> Jhant pKd ke bhaga Aage")
                    dest = self.board.get_ladder_dest(pos)
                    print(f' you climb to {dest}')
                    player.position = dest
                else:
                    dest = pos
                print(f' Your Lates Position is {dest}')
                player.position = dest
                if dest >= self.board.size:
                    print(f'Hurray !! {player.username}win.')
                    CONTINUE = False
                    break
