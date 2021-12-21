import random

rps = ['Rock', 'Paper', 'Scissors']
print(type(rps))

pc = random.choice(rps)  

human = []
print(rps)
for choice in rps:
    print(choice)
    
human = input("Enter your selection: ")
if human == pc:
    print("Computer picked: ", pc)
    print("You picked: ", human)
    print("It is a tie.\n")
elif human == 'Rock' and pc == 'Paper':
    print("Computer picked: ", pc)
    print("You picked: ", human )
    print("Paper covers rock: You lost.\n")
elif human == 'Rock' and pc == 'Scissors':
    print("Computer picked: ", pc)
    print("You picked: ", human)
    print("You crushed the Scissors: You won!\n")
elif human == 'Paper' and pc == 'Rock':
    print("Computer picked: ", pc)
    print("You picked: ", human)
    print("Paper covers Rock : You won!\n")
elif human == 'Paper' and pc == 'Scissors':
    print("Computer picked: ", pc)
    print("You picked: ", human)
    print("Scissors cut the Paper: You lost.\n")
elif human == 'Scissors' and pc == 'Rock':
    print("Computer picked: ", pc)
    print("You picked: ", human)
    print("Scissors got crushed by Rock: You lost.\n")
elif human == 'Scissors' and pc == 'Paper':
    print("Computer picked: ", pc)
    print("You picked: ", human)
    print("You cut the Paper: You won!\n")



