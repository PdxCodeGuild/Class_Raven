## Project Overview

Web application designed for physical key inventory and control. Any organization that has to deal with a large amount of keys/access badges must have a solution to keep track of them. Not having the ability to do so greatly reduces a facilities physical security. I plan on using Django framework to build this web app. 

## Functionality

A non-admin user will be able to log in and view the keys or badges that are assigned to them. They will also be able to digitally sign for them. Admin users are responsible for entering keys/badge ID/Descriptions into the database and maintaining control over them. They will issue keys to registered users and ensure the user digitally signs for them. There will bne a search function to look up a specific key ID that will display all data on that key.

## Data Model

There will be at least 3 data tables. One for the master key list, users, and key issuing. The key issuing table will be the joining table between the other table with a one to many relationship

| 1. key_list |
- key_id       
- key_for      
- available_status
              
| 2. key_issue |
- key_id
- key_user
- issue_date
- user_sign_date
- return_due_date

| 3. key-user |
- user_id
- user_name|

## Schedule

- 23-29 Jan: Models/Data tables for keys
- 30-05 Feb: Models/Data tables users
- 06-12 Feb: Models/Data tables key issue/return
- 13-19 Feb: Styling and additional features
- 20-23 Feb: Final touches/checks and presentation.
- 23 Feb and on: I plan on polishing up this project and putting it to use in a real world environment. The next project will be a time and addendance application wher employees and request time off and certify their pay. The supervisor will have approval, editing, certification permissions.