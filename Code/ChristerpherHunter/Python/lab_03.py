from random import randint

def main() -> None:

    def converter(score: int) -> str:

        plus_or_minus = score % 10

        if score > 89:
            temp_grade = "A"
        elif score > 79:
            temp_grade = "B"
        elif score > 69:
            temp_grade = "C"
        elif score > 59:
            temp_grade = "D"
        else:
            temp_grade = "F"

        if plus_or_minus > 5:
            return f"{temp_grade}+"
        elif plus_or_minus < 5:
            return f"{temp_grade}-"
        else:
            return f"{temp_grade}"
        

    user_score = input("Please enter a numerical grade: ")
    if not user_score.isnumeric():
        print("\nINVALID ENTRY, INTEGERS ONLY\n")
        exit()  

    

    rival_score = randint(45, 100)

    print(f"Your letter grade is: {converter(int(user_score))}\n")
    print(f"Your rival's score is: {rival_score}\n")

    if rival_score > int(user_score):
        print("Your rival has bested you!")
    else:
        print("You have bested your rival!")




if __name__ == '__main__':
    main()