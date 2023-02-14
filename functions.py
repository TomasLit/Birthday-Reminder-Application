# In this file I keep functions that I use in multiple .py files


# Function that writes a log when program starts
def log():
    from datetime import datetime
    from constants import LOGS_ERR_PATH

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGS_ERR_PATH, "a") as file:
        file.write("\n")
        file.write("Program started at - " + now + "\n")


# Write the time the program finished the work
def last_log():
    from datetime import datetime
    from constants import LOGS_ERR_PATH

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGS_ERR_PATH, "a") as file:
        file.write("Program finished at - " + now + "\n")



# Function that creates login.csv file where users e-mail server data is saved
def create_login_file():
    import csv
    from constants import LOGIN_PATH

    print("To send e-mails the program needs to collect your e-mail server data: \n")

    # Creating the CSV file and writing the header row
    with open(LOGIN_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["login", "password", "host", "port", "sender_email"])
            
        # Prompt the user for the data
        login = input("Enter login: ")
        password = input("Enter password: ")
        host = input("Enter host: ")
        port = input("Enter port: ")
        sender_email = input("Enter sender_email: ")
        print("")
            
        # Write the data to the CSV file
        writer.writerow([login, password, host, port, sender_email])