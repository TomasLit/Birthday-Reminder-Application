import csv
import datetime
from check_errors import data_file


now = datetime.datetime.now()
now_formatted = now.strftime("%m-%d")
now_datetime = datetime.datetime.strptime(now_formatted, "%m-%d")
week = datetime.timedelta(days=7)


# Creating the list where all birthdays 
upcoming_birthdays = []


with open(data_file, 'r') as file:
    reader = csv.reader(file)
    # skip the first row with headers
    headers = next(reader) 
    birthdate_index = headers.index('birthdate')

    # Checking what birthdays will be in a week
    for row in reader:
        name, email, birthdate = row
        birthdate = datetime.datetime.strptime(row[birthdate_index], '%m-%d')
        days_left = birthdate - now_datetime
        if days_left == week:
            print(days_left, " == ", week)
            upcoming_birthdays.append(name)
            print(upcoming_birthdays)   


# Checking if there is a need to send reminding letters 
count = len(upcoming_birthdays)
if count > 0:
    print("upcoming_birthdays = ", count, upcoming_birthdays)
    import send_letter
else:
    print("There are no upcoming birthdays")




















