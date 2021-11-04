"""
Christerpher Hunter
Lee Colburn
Aaron Quiroz

Lab 20: Adventure Game

Create a Character and Enemy class.

Create a game board with a list of lists.

Randomly place enemies on the board.

Write a REPL that allows the character to move around
the board until they encounter an enemy, then battle
the enemy until one of the characters is defeated.

If the character defeats all the enemies, they win. Otherwise, they lose.
"""

from random import randint
from colorama import Fore as F

R = F. RESET


class Character:
    """Character on the game board"""

    def __init__(self) -> None:

        self.position_x = int()
        self.position_y = int()
        self.height = 10
        self.width = 10

    def game_board(self) -> list:
        """Set the board"""

        board = []  # start with an empty list
        for i in range(self.height):  # loop over the rows
            board.append([])  # append an empty row
            for _ in range(self.width):  # loop over the columns
                board[i].append("[ ]")  # append an empty space to the board

        return board


class Enemy(Character):
    """Enemy of the Character"""

    def __init__(self) -> None:

        super().__init__()


def main() -> None:

    player = Character()

    board = player.game_board()

    player.position_x = 4
    player.position_y = 4

    enemy = Enemy()

    for _ in range(4):
        enemy.position_x = randint(0, enemy.height - 1)
        enemy.position_y = randint(0, enemy.width - 1)
        board[enemy.position_x][enemy.position_y] = "[§]"

    game_tracker = int()
    while game_tracker != 4:

        for i in range(player.height):
            for j in range(player.width):
                # if we're at the player location, print the player icon
                if i == player.position_x and j == player.position_y:
                    print("[☺]", end=" ")
                else:
                    # otherwise print the board square
                    print(board[i][j], end=" ")
            print()

        # get the command from the user
        command = input("what is your command? ")

        if command == "done":
            break  # exit the game
        elif command == "l":
            player.position_y -= 1  # move left
        elif command == "r":
            player.position_y += 1  # move right
        elif command == "u":
            player.position_x -= 1  # move up
        elif command == "d":
            player.position_x += 1  # move down

        match player.position_x:
            case -1:
                print(f"{F.RED}BATTLEFIELD LIMIT REACHED{R}")
                player.position_x += 1
            case 10:
                print(f"{F.RED}BATTLEFIELD LIMIT REACHED{R}")
                player.position_x -= 1

        match player.position_y:
            case -1:
                print(f"{F.RED}BATTLEFIELD LIMIT REACHED{R}")
                player.position_y += 1
            case 10:
                print(f"{F.RED}BATTLEFIELD LIMIT REACHED{R}")
                player.position_y -= 1

        # check if the player is on the same space as an enemy
        if board[player.position_x][player.position_y] == "[§]":
            print(f"{F.YELLOW}You've encountered an enemy!{R}")
            action = input("what will you do? ")
            if action == "attack":
                print(f"{F.GREEN}You've slain the enemy{R}")
                game_tracker += 1
                # remove the enemy from the board
                board[player.position_x][player.position_y] = "[ ]"
            else:
                print(f"{F.RED}You hestitated and were slain!{R}")
                break

                # print out the board


if __name__ == "__main__":
    main()
