
# Define the directory and name of data file e-mail server information will be saved 
login_file_path = 'Data files/login.csv'

# Directory of the data file with all of information
contacts_file = "Data files/contacts.csv"

# Name of a file that holds all logs and errors
logs_errors = "logs_and_errors.txt"


# Function that logs when program starts
def log():
    from datetime import datetime

    # Write the time the program started
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logs_errors, "a") as file:
        file.write("\n")
        file.write("Program started at - " + now + "\n")


# Function that creates login.csv file where users e-mail server data is saved
def create_login_file():
    import csv

    print("To send e-mails the program need to collect your e-mail server data: \n")
    # Creating the CSV file and writing the header row
    with open(login_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'password', 'host', 'port', 'sender_email'])
            
        # Prompt the user for the data
        login = input("Enter login: ")
        password = input("Enter password: ")
        host = input("Enter host: ")
        port = input("Enter port: ")
        sender_email = input("Enter sender_email: ")
        print("")
            
        # Write the data to the CSV file
        writer.writerow([login, password, host, port, sender_email])