# Birthday-Reminder-Application

Task of the program is to remind by e-mail a number of people about upcoming birthdays. The information about those people are stored in "contacts.csv" file located in "Data files" folder. 

To start the program installation guide - run the "Birthday Reminder App.py". In this process you will have to write your e-mail server information which will be stored in newly created login.csv file. If the file is already created you would be able to keep it like that or overwrite the information inside it. After that the program will give you a menu to choose what you want to do next. Options:

1. To [C]reate a new task in Windows Task Scheduler so the program would run daily. 
2. To [D]elete previously written task in Windows Task Scheduler. 
3. To [S]end birthday reminding letters right now.
4. To [O]pen logs_and_errors file. 
5. To [R]ead instruction how to manually create a daily task in Windows Task Scheduler.
6. To [Q]uit.

There is a way to run the program bypassing the installation file. To do so, you need to run the "check_errors.py" file. It will check "contacts.csv" for errors. And will create "logs_and_errors.txt" file. It will write a new log every time the program has ran. If there are any errors it will write them into logs_and_errors.txt file as well. After checking the contacts.csv file for errors it will count errors and if there are non then it will initiate the "check_data_for_birthdays.py" file. This file will check if there are any persons from the data file whose birthday will be in a week. And if it founds any it will write it to the "upcoming_birthdays" list and initiate "send_letters.py" file. This file will send letters to all of the people who are in the "contacts.csv" except for the one whose birthday is coming. If there are more then one human with birthday on the same day it will send as many letters to the people from the "contacts.csv" as there are birthdays that day. 

Program have been tested using development server at https://develmail.com/. The results can be seen at the attached screenshot.