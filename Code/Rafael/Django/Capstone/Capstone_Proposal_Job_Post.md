___
## Project Overview

A job posting site for the general public to use for free like craigslist.  

Any user can view the postings but would not have the ability to see contact info, be able to message or follow another user in the detail page unless the user is logged in and registered.

Also a user will not be able to create a posting unless they are logged in and registered. 

The layout is going to be blog like with small cards that expand into a full-page view with more details about specific job parameters and a section to email or message them on the site.   

This will be a Django based project using Python3, HTML, CSS and JAVASCRIPT. It will be mostly Bootstrap and flex-box box styled with custom css and javascript for better visuals.

___

## Functionality

A pop up will require the user to be 16 years or older to continue. A user will be able to look up job posting that are stored in the database without a login. They will see the most recent job posts added by date. A side-bar will have a search query to **type a search for keywords** along **other search query fields.**

A user will however need to make an account and login if they are to post a job search. A user will able to add a job with required fields in place. *-Job Title*, *-Job Description Keywords*, *-Skills / Proficiencies*, *-State*, *-City*, *-shift (day, evening, night)*, *-hours (full-time, part-time, short-term/seasonal)*, *-remote (yes, no, no-preference )*, *-availability (now, 1-2months, 3-4 months, 5-6 months)*.

___

## Data Model

The main model will include:

User
+ *Picture*[models.ImageField] (*optional)
+ *user name* [forms.CharField()]

Job App
+ *Job Title* [forms.CharField()]
+ *Job Description Keywords* [forms.CharField()]
+ *Position Title* [forms.CharField()]
+ *Skills / Proficiencies* [forms.CharField()]
+ *State* [forms.CharField()]
+ *City* [forms.CharField()]
+ *shift (day, evening, night)* [forms.NullBooleanField()]
+ *hours (full-time, part-time, short-term/seasonal)* [forms.NullBooleanField()]
+ *remote (yes, no, no-preference)* [forms.NullBooleanField()forms.NullBooleanField()]
+ *availability (ASAP, 1-2months, 3-4 months, 5-6 months)* [forms.NullBooleanField()]
+ *created date*[forms.DateField()]


___

## Schedule

**Weeks**

*Note: This will change along the process.

- 1st week
    - basic Django 
    - setup Project, App, Superuser
    - create models 
    - migrate 
    - create views
    - create templates
    - create urls
    - create Forms
    - test Data Response
    - create database(s) for job fields
    - test database retrieval
    - troubleshooting 
- 2nd week
    - bootstrap layouts home page and creation page
    - create user profiles with job fields content
    - create user options (delete & update)
    - set up user (following)
    - troubleshooting  
- 3rd week
    - set-up messaging
    - work on the front-end layout and styles
    -troubleshooting
- 4th week
    - troubleshooting
    - testing 
    - if there is time add functionality to be able to post job opening from employers/recruiters.
    - finalize 


___

