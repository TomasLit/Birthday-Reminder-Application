import csv
import os
from datetime import datetime
from constants import contacts_file
from constants import login_file_path
from constants import logs_errors
from constants import log
from constants import create_login_file


def start_app():
    if os.path.exists(login_file_path):
        print("file exists")
        return
    else:
        print("need to create new file")
        create_login_file()


def log_error(error):
    # Append the error to the errors.csv file
    with open(logs_errors, "a") as file:
        file.write(error + "\n")


# Creating list where errors will be stored
errors = []


def count_rows(file_path):    
    # Read the cvs file
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            
            # Count the number of rows. There should be no more than 100 rows with entries.
            row_count = sum(1 for row in reader)
            print(row_count)
            if row_count > 100:
                errors.append("Data file has more than 100 entries! Please delete extra entries.")

    except Exception as e:
        errors.append(str(e))
        log_error(str(e)) 


def check_file(file_path):

    # Read the cvs file
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            required_columns = ["name", "email", "birthdate"]
            
            # Check if all required columns are present
            if any(col not in headers for col in required_columns):
                errors.append("Data file is missing required columns")            

            for i, row in enumerate(reader):
                # Check if all required fields are present
                if len(row) != len(headers):
                    errors.append(f"Row {i + 1} is missing required fields")
                
                # Check if name, email and birthday fields are not empty
                name, email, birthdate = row
                if not name:
                    errors.append(f"Name is not set for '{email}'")
                if not email:
                    errors.append(f"Email is not set for '{name}'")
                if not birthdate:
                    errors.append(f"Birthdate is not set for '{name}'")  
                
                # Check if birthdate format is valid
                try:
                    birthdate = datetime.strptime(birthdate, "%m-%d")
                except ValueError:
                    errors.append(f"Invalid birthdate format for '{name}'")

    except Exception as e:
        log_error(str(e)) 
    
    for error in errors:
        log_error(error)


# Writing then the program started
try:
    start_app()
    print("Login file exists")
except Exception as e:
    print(e)

# Writing then the program started
try:
    log()
    print("Logging done")
except Exception as e:
    print(e)

# Counting the rows
try:
    count_rows(contacts_file)
    print("Rows counted")
except Exception as e:
    print(e)

# Checking data
try:
    check_file(contacts_file)
    print("File checked")
    print(errors)
except Exception as e:
    print(e)

# Checking if there are errors and proceeding or stopping the program
count = len(errors)
print("Number of errors = ", count)
if count > 0:
    text = """There are errors in the data file. Please correct data file before running program 
again. You can find information about all errors in logs_and_errors.txt file """
    with open(logs_errors, "a") as file:
        file.write(text + "\n")
    print(text)

else:
    import check_data_for_birthdays