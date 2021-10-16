# Aaron lab2
#convert dollar amount into number of coins

user_input = input('Enter a dollar amount: ')

#userinput makes pennies
pennies = float(user_input) * 100
#finding number of quarters 
quarters = pennies//25
#removing total of quarters from pennies
remainder = pennies-quarters * 25

dimes = remainder//10

remainder_ = remainder-dimes * 10

nickels = remainder_//5

remainder_five = remainder_-nickels *5

penny= remainder_five//1

remainder_one = remainder_five-penny *1

print(f'{int(quarters)} quarters, {int(dimes)} dime, {int(nickels)} nickels, {int(penny)} penny')