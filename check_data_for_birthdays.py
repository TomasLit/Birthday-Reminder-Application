import csv
import datetime
from constants import CONTACTS_PATH
from constants import LOGS_ERR_PATH
from functions import last_log


# Capturing current date
now = datetime.datetime.now()
now_formatted = now.strftime("%m-%d")
now_datetime = datetime.datetime.strptime(now_formatted, "%m-%d")

# Calculating a week
week = datetime.timedelta(days=7)

# Creating the list where all birthdays will be stored
upcoming_birthdays = []


# Reading csv file
with open(CONTACTS_PATH, "r") as file:
    reader = csv.reader(file)
    headers = next(reader) 
    birthdate_index = headers.index("birthdate")

    # Checking what birthdays will be in a week
    for row in reader:
        name, email, birthdate = row
        birthdate = datetime.datetime.strptime(row[birthdate_index], "%m-%d")
        days_left = birthdate - now_datetime
        if days_left == week:
            upcoming_birthdays.append(name)


count_bir = len(upcoming_birthdays)

if count_bir == 0:

    text = "There are no upcoming birthdays! \n"
    with open(LOGS_ERR_PATH, "a") as file:
        file.write(text)
    print(text)

    last_log()