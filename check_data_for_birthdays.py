import csv
import datetime
from constants import contacts_file
from constants import logs_errors


# Capturing current date
now = datetime.datetime.now()
now_formatted = now.strftime("%m-%d")
now_datetime = datetime.datetime.strptime(now_formatted, "%m-%d")

# Calculating a week
week = datetime.timedelta(days=7)

# Creating the list where all birthdays will be stored
upcoming_birthdays = []


# Reading csv file
with open(contacts_file, "r") as file:
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


# Checking if there is a need to send reminding letters 
count = len(upcoming_birthdays)
if count > 0:
    text = "Number of upcoming birthdays = " + str(count) + "\n"
    with open(logs_errors, "a") as file:
        file.write(text)
    print(text)
    import send_letters
else:
    text = "There are no upcoming birthdays! \n"
    with open(logs_errors, "a") as file:
        file.write(text)
    print(text)