# Christerpher Hunter
# Lab 05: Rock Paper Scissors

from random import randint
from colorama import Fore as F

R = F.RESET

class RPS:

    def __init__(self) -> None:
        self.cpu_rock = ""
        self.cpu_paper = ""
        self.cpu_scissors = ""
        self.usr_rock = ""
        self.usr_paper = ""
        self.usr_scissors = ""
    
    # Get user input
    def get_user_choice(self) -> str:
        
        usr_pick = ""
        # Check if input is valid
        while usr_pick not in ['rock', 'paper', 'scissors']:
            usr_pick = input("\nPlease choose\nrock\npaper\nscissors\n\nChoice: ")    
            print(f"{F.RED}error, invalid input. Choose again\n{R}")
                    
        match usr_pick:
            case "rock":
                self.usr_rock = "rock"
                return self.usr_rock
            case "paper":
                self.usr_paper = "paper"
                return self.usr_paper
            case "scissors":
                self.usr_scissors = "scissors"
                return self.usr_scissors            

    
    # Get computer choice
    def get_cpu_choice(self) -> str:
        cpu_pick = randint(1,3)
        
        match cpu_pick:
            case 1:
                self.cpu_rock = "rock"
                return self.cpu_rock
            case 2:
                self.cpu_paper = "paper"
                return self.cpu_paper
            case 3: 
                self.cpu_scissors = "scissors"
                return self.cpu_scissors


    # Determine the winner
    def determine_winner(self,cpu_results: str, usr_results: str) -> str:

        results_tuple = (cpu_results, usr_results)
               
        match results_tuple:
            case ("rock", "paper"):
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\n\
{F.RED}CPU wins!{R}"
                return result
            
            case ("rock", "scissors"):
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\n\
{F.RED}CPU wins!{R}"
                return result
            
            case ("paper", "rock"):
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\n\
{F.GREEN}USER wins!{R}"
                return result

            case ("paper", "scissors"):
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\n\
{F.GREEN}USER wins!{R}"
                return result
            
            case ("scissors", "rock"):
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\n\
{F.GREEN}USER wins!{R}"
                return result
            
            case ("scissors", "paper"):
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\
{F.RED}CPU wins!{R}"
                return result
            
            case _:
                result = f"Computer picks {F.CYAN}{cpu_results}{R}\n\
User picks {F.CYAN}{usr_results}{R}\n\n\
{F.YELLOW}IT's a TIE!{R}"
                return result


def main() -> None:

    print(f"\n\n{F.GREEN}Welcome to Rock, Paper, Scissors Game!{R}")
    print(f"\nYou will be playing against the Computer.")

    game_1 = RPS()

    # While loop to allow replays
    val = True
    while val == True:

        # Get the user's choice
        user_pick = game_1.get_user_choice()

        # Get the CPU's choice
        cpu_pick = game_1.get_cpu_choice()

        print("\n")

        # Determine the winner
        result = game_1.determine_winner(cpu_pick, user_pick)

        print(result)

        play_again = input(f"\n\nType {F.MAGENTA}'yes'{R} if you would like to play again,\
 otherwise press {F.RED}ENTER{R} to exit\nChoice: ")
        
        match play_again:
            case "":
                val = False
            case "yes":
                val = True
            case _:
                print(f"{F.RED}Invalid entry! GAME OVER!{R}")
                val = False

if __name__ == '__main__':
    main()


