# Birthday-Reminder-Application

Task of the program is to remind by e-mail a number of people about upcoming birthdays. The information about those people are stored in "contacts.csv" file located in "Data files" folder. 

To start the program installation guide - run the "Birthday Reminder App.py". In this process you will have to write your e-mail server information which will be stored in newly created login.csv file. If the file is already created you would be able to keep it like that or overwrite the information inside it. After that the program will ask if you want to create a task in Windows Task Scheduler for the program to run daily or you want to delete previously created task in Windows Task Scheduler? If you will choose to create new task - after the creation of the task will be finished you will also see an instruction how to create task in Windows Task Scheduler manually in case it wouldn't work other way. 

To start the program immediately run the "check_errors.py" file. It will check "contacts.csv" for errors. And will create "logs_and_errors.txt". It will write a new log every time the program has ran. If there are any errors it will write them into this .txt file as well. After it will check the contacts.csv file for errors ir will count errors and if there are non then it will initiate the "check_data_for_birthdays.py" file. This file will check if there are any persons from the data file whose birthday will be in a week. And if it founds any it will write it to the "upcoming_birthdays" list and initiate "send_letters.py" file. This file will send letters to all of the people who are in the "contacts.csv" except for the one whose birthday is coming. If there are more then one human with birthday on the same day it will send as many letters to the people from the "contacts.csv" as there are birthdays that day. 

Program have been tested using development server at https://develmail.com/. The results can be seen at the attached screenshot.