## Project Overview

Web application designed for physical key inventory and control. Any organization that has to deal with a large amount of keys/access badges must have a solution to keep track of them. Not having the ability to do so greatly reduces a facilities physical security. I plan on using Django framework to build this web app. 

## Functionality

A non-admin user will be able to log in and view the keys or badges that are assigned to them. They will also be able to digitally sign for them. Admin users are responsible for entering keys/badge ID/Descriptions into the database and maintaining control over them. They will issue keys to registered users and ensure the user digitally signs for them. There will bne a search function to look up a specific key ID that will display all data on that key.

## Data Model

There will be at least 3 data tables. One for the key type, key details, and specific copies. There will be no model for users as the Django admin will manage that.

| 1. KeyType | (e.g. Vehicle, Door , Locker, Padlock)
- name = models.CharField

| 1. KeyId | (Key details)
- title = models.CharField
- summary = models.TextField
- usefor = models.ManyToManyField (can have many key types with multiple copies)
              
| 3. KeyInstance | (Specific copies)
- id = models.CharField
- key = models.ForeignKey (uses KeyId)
- due_back = models.DateField

## Schedule

- 23-29 Jan: Models/Data tables for key library
- 30-05 Feb: Add features for users to reserve and loan keys.
- 06-12 Feb: Complete a minimum viable product and begin styling
- 13-19 Feb: Finish styling and add any desired features. 
- 20-23 Feb: Final touches/checks and presentation.
- 23 Feb and on: I plan on polishing up this project and putting it to use in a real world environment. The next project will be a time and addendance application wher employees and request time off and certify their pay. The supervisor will have approval, editing, certification permissions.