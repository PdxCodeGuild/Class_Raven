print("Make Change Tool")
amount = input("what is the Dollar amount?\n>")
amount2 = float(amount)

amount2 = amount2 * 100
amount2 = int(amount2)

print(f"${amount} converts to;")

quarters = amount2 // 25

if quarters != 0:
    print(f"{quarters} Quarters")
remainder = amount2 % 25

dimes = remainder // 10

if dimes != 0:
    print(f"{dimes} Dimes")
remainder2 = remainder % 10

nickels = remainder2 // 5

if nickels != 0:
    print(f"{nickels} Nickels")

pennies = remainder2 % 5

if pennies != 0:
    print(f"{pennies} Pennies")

#not very elegant.