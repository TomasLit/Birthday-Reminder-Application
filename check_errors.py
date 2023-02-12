import csv
from datetime import datetime


# Directory of the data file with all of information
data_file = "Data files/contacts.csv"


def log():
    # Write the time the program started
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('logs_and_errors.txt', 'a') as file:
        file.write("\n")
        file.write("Program started at - " + now + "\n")


def log_error(error):
    # Append the error to the errors.csv file
    with open('logs_and_errors.txt', 'a') as file:
        file.write(error + "\n")


# Creating list where errors will be stored
errors = []


def count_rows(file_path):    
    # Read the cvs file
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            
            # Count the number of rows
            row_count = sum(1 for row in reader)
            print(row_count)
            if row_count > 100:
                raise Exception("Data file has more than 100 entries! Please delete extra entries.")

    except Exception as e:
        errors.append(str(e))
        log_error(str(e)) 


def check_file(file_path):

    # Read the cvs file
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            required_columns = ['name', 'email', 'birthdate']
            
            # Check if all required columns are present
            if any(col not in headers for col in required_columns):
                raise Exception("Data file is missing required columns")            

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
                    birthdate = datetime.strptime(birthdate, '%m-%d')
                except ValueError:
                    errors.append(f"Invalid birthdate format for '{name}'")

    except Exception as e:
        log_error(str(e)) 
    
    for error in errors:
        log_error(error)


# Writing then the program started
try:
    log()
    print("Logging done")
except Exception as e:
    print(e)

# Counting the rows
try:
    count_rows(data_file)
    print("Rows counted")
except Exception as e:
    print(e)

# Checking data
try:
    check_file(data_file)
    print("File checked")
    print(errors)
except Exception as e:
    print(e)

# Checking if there are errors and proceeding or stopping the program
count = len(errors)
print("number of errors = ", count)
if count > 0:
    print("There are errors in the data file. Please correct data file before running program. You can find information about all errors in logs_and_errors.txt file ")
else:
    import check_data