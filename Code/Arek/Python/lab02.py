#I always copy and paste the lab into the file just so I dont have to go back and forth


"""

Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, 
the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, 
resulting in the fewest amount of coins. First convert the dollar amount (1.36) into the total number of pennies (136), 
then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Enter a dollar amount: 1.36
5 quarters, 1 dime, and 1 penny

Enter a dollar amount: 0.67
2 quarters, 1 dime, 1 nickel, 2 pennies

Version 2 (optional)

Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

"""

# getting the total dollar amount from the user
total = input("Please enter a dollar amount: ")
#using the .replace just because it was easier for me to work with numbers without the decimals in them
total = total.replace(".", "")
# had to convert it into an integer last since .replace() does not work with integer data types
total = int(total)

#just setting the values for all the coins
quarter = 25
dime = 10
nickel = 5
penny = 1

#line 43 is getting the total amount of quarters possible in the given dollar amount, its important that this is correct as all other lines follow suit
quarters = total // quarter
#to know how many other coins can go into the total besides quarters(if possible), we have to subtract the value of all the quarters from the total dollar amount
total %= quarter
#lines 48-53 are doing the same concept as line 45
dimes = total // dime
total %= dime
nickles = total // nickel
total %= nickel
pennies = total // penny
total %= penny

#this is just to show the user how many coins go into their input dollar amount
print(f"{quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies")

#will attempt version 2 at a later time










        










