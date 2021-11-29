# Mini Python Capstone
#Key Log

import csv
from tabulate import tabulate
file_content = []

print("███ Current Key Log ███")

with open ('keys_doc.csv','r') as file:
   key_file =csv.reader(file)
   for row in key_file:
      file_content.append(row)

print(tabulate(file_content, tablefmt="grid"))
#print(file_content)

menu_options = {
    '1': 'Update',
    '2': 'New Issue',
    '3': 'Exit'}

while True:

    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input('Enter the number of the option you would like to perform: ')

    if command == '1':

        editRow = int(input("\nWhich row would you like to change? Enter 1 - " + str(len(file_content)-1) + " :"))
        print ("Please enter the new details for each of the following :")

        for i in range (len(file_content[0])):
            new_details = input("Enter new data for " + str(file_content[0][i]) + " :")
            file_content[editRow][i] = new_details

        print ("\nPlease see the details of the new file below:")
        for i in range (len(file_content)):
            print ("Row " + str(i) + " :" + str(file_content[i]))

        changeCSV = input ("\nWould you like to make the changes to the csv file ? Y/N").lower()

        if changeCSV == ("y"):
            with open ('keys_doc.csv','w+') as file:
                key_file = csv.writer(file)
                for i in range (len(file_content)):
                    key_file.writerow(file_content[i])
                  
    elif command == '2':

        my_file = open("keys_doc.csv")
        string_list = my_file.readlines()

        with open ('keys_doc.csv','w+') as file:
            #key_file =csv.reader(file)
            #for row in key_file:
            #    file_content.append(row)

#                editRow = int(input("\nWhich row would you like to add? Enter 1 - " + str(len(file_content)-1) + " :"))
#                print ("Please enter the new details for each of the following :")
            new_input = []
            for i in range (len(file_content[0])):
                new_details = input("Enter new data for " + str(file_content[0][i]) + " :")
                new_input.append(new_details)

                print ("\nPlease see the details of the new file below:")
                for i in range (len(new_input)):
                    print ("Row " + str(i) + " :" + str(new_input[i]))

            changeCSV = input ("\nWould you like to make the changes to the csv file ? Y/N").lower()

            if changeCSV == ("y"):
                with open ('keys_doc.csv','w+') as file:
                    key_file = csv.writer(file)
                    for i in range (len(file_content)):
                        key_file.writerow(file_content[i])
                #    file.write(str(new_input))

    elif command == '3':
        break
 