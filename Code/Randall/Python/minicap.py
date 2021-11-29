#Mini Python Capstone 

#create REPL // ATm lab has a good example
import csv
from tabulate import tabulate 

file_content = []

print("███ Current Key Log ███")

with open('keys_doc.csv', 'r') as file:
    key_file = csv.reader(file)
    for row in key_file:
        file_content.append(row)
print(tabulate(file_content, headers=["Issue to", "Issuer", "Key Number", "Key For", "Date Out", "Date In"], tablefmt="grid"))

#print("See Key Control data below")
#for i in range(len(file_content)):
#   print(("Row" + str(i + 1) + ": " + str(file_content[i][0])))

menu_options = {
    '1': 'Update',
    '2': 'New Issue',
    '3': 'Exit'
}

while True:
    file_content = []

    print()
    for menu, option in menu_options.items():
        print(f'{menu}. {option}')  

    selection = input('\nEnter the number of the option you would like to perform\n> ')
    selection = menu_options.get(selection)

    if selection == 'Update':
        update = int(input("Which row would you like to change? Enter 1 - " + str(len(file_content)) + " :"))
        print("Please enter the new details for each of the following :")

        for i in range(len(file_content[0])):
            updated_data = input("Enter new details for " + str(file_content[0][i]) + " :")
        file_content[update][i] = updated_data

        print(("Please see new file below: "))
        for i in range(len(file_content)):
            print("Row " + str(i) + " :" + str(file_content[i]))

#    elif selection == 'New Issue':







"""
update = int(input("Which row would you like to change? Enter 1 - " + str(len(file_content)) + " :"))
print("Please enter the new details for each of the following :")

for i in range(len(file_content[0])):
    updated_data = input("Enter new details for " + str(file_content[0][i]) + " :")
    file_content[update][i] = updated_data

print(("Please see new file below: "))
for i in range(len(file_content)):
    print("Row " + str(i) + " :" + str(file_content[i]))

changeCSV = input("Would you like to update the key roster? Y/N: ").lower()
if changeCSV == ("y"):
    with open("keys_doc.csv", "w+") as file:
        key_file = csv.writer(file)
        for i in range(len(file_content)):
            key_file.writerow(file_content[i])
#else:
 #    print("Goodbye")
"""