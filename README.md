# Birthday-Reminder-Application

In "Contacts" folder there is a "contacts.cvs" file with all the data we need: name, e-mail and birthdate.

Run the "check_errors.py" file. It will check "contacts.cvs" for errors. And will create "logs_and_errors.txt". It will write a new log everytime the program is runned. If there are any errors it will write them into this .txt file. If there are any ir will initiate the "check_data.py" file. This file will check if there are any persons from the data file whose birthday will be in a week. And if it founds any it will write it to the "upcoming_birthdays" list and initiate "send_letter.py" file. This file will send letters to all of the people who are in the "contacts.cvs" except for the one whose birthday is comming. If there are more then one human with birthday on the same day it will send as many letters to the people from the "contacts.cvs" as there are birhtdays that day. 
