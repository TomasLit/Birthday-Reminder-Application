import subprocess
import os
import csv
import sys
from datetime import datetime


# Define the task name
task_name = "Birthday reminder app"

# Define the directory and name of data file e-mail server information will be saved 
file_path = 'Data files/login.csv'

# Introduction to the App
print("B I R T H D A Y   R E M I N D E R   A P P \n")
print("Welcome to Birthday Reminder App! Please follow the installation instructions below.\n")


# Function that creates login.csv file where users e-mail server data is saved
def create_login_file():
    print("To send e-mails the program need to collect your e-mail server data: \n")
    # Creating the CSV file and writing the header row
    with open(file_path, 'w', newline='') as file:
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


# Function that creates or deletes a daily task in Windows Task Scheduler
def task():
    task = input("If you want to write program as the task to Windows Task Scheduler so the program would run daily in automatic mode write letter W and press Enter. If you want to delete previously written task in Windows Task Scheduler write letter D and press Enter ")
    print("")

    if task == "w" or task == "W":
        while True:
            time_input = input("Enter the time in the format 'HH:MM': ")
            try:
                time = datetime.strptime(time_input, '%H:%M').time()
                break
            except ValueError:
                print("Error: Invalid time format. Please try again.")
        
        file_name = "check_errors.py"
        program = "schtasks"
        arguments = ['/create', '/tn', task_name, '/tr', f'{sys.executable} {file_name}', '/sc', 'daily', '/st', time.strftime('%H:%M')]
        start_in = os.path.dirname(os.path.abspath(__file__))
        return_code = subprocess.call([program] + arguments, cwd=start_in)

        if return_code == 0:
            print("Task was successful created!")
        else:
            print("Error during installation. Return code: ", return_code)
        
        # Instruction how to manually create a daily task in Windows Task Scheduler 
        print("")
        print("In case the Windows Task Scheduler would not run Python files (sometimes Windows for security reasons can block exection of the files) you can write the program to Windows Task Scheduler manually. Below you will find the instruction for that. \n")
        print("Go to the start menu and search for \"task sheduler\". Then open it. \n")
        print("In the upper left corner select \"Action\" and \"Create Task\". \n")
        print("In the \"General\" segment write the name of the task. It doesn't matter how you will call it. \n")
        print("In the \"Triggers\" segment push \"New\" and select the time and how often you would like the App would remind about birthdays. \n")
        print("In the \"Actions\" segment push \"New\" and then: \n")
        print("In the \"Program/script\" line write: ", sys.executable, "\n")
        print("In the \"Add arguments\" line write: check_errors.py \n")
        print("In the \"Start in\" line write: ", os.path.dirname(os.path.abspath(__file__)))
        print("\n")

    elif task == "d" or task == "D":
        return_code = subprocess.call(['schtasks', '/delete', '/tn', task_name, '/f'])
        if return_code == 0:
            print("Task was successfully deleted. \n")
        else:
            print("Error: Task was not deleted. Most likely it wasn't created before. Error return code:", return_code, "\n")   
    else:
        print("")
        print("You have selected wrong letters, please try again! \n")
        return task()

def start_app():
    if os.path.exists(file_path):
        login_file_found = input("Program found your e-mail server information from the previous session. Would you like to keept it or overwrite it? [K]eep or [O]verwrite? ")
        print("")
        if login_file_found == "K" or login_file_found == "k":
            task()
        elif login_file_found == "O" or login_file_found == "o":
            create_login_file()
            task()
        else:
            print("You have selected wrong letters, please try again! \n")
            start_app()
    else:
        create_login_file()
        task()
start_app()