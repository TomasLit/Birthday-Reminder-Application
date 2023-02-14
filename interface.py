import subprocess
import os
import sys
from datetime import datetime
from constants import LOGS_ERR_PATH
from constants import MAIN_DIRECTORY
from functions import create_login_file


# Task name in case it would be written as task to Windows Task Scheduler
task_name = "Birthday reminder app"

# Introduction to the App
def intro():
    print("B I R T H D A Y   R E M I N D E R   A P P \n \n")
    print("Welcome to Birthday Reminder App! Please follow the installation instructions below.\n")


# Function that creates or deletes a daily task in Windows Task Scheduler
def function_task():
    print("To [C]reate a new task in Windows Task Scheduler so the program would run daily write letter - C")
    print("To [D]elete previously written task in Windows Task Scheduler write letter - D")
    print("To [S]end birthday reminding letters right now press letter - S")
    print("To [I]mplement new e-mail server information press letter - I") 
    print("To [O]pen logs_and_errors file press letter - O")
    print("To [E]rase logs_and_errors file press letter - E")      
    print("To [R]ead instruction how to manually create a daily task in Windows Task Scheduler press - H")
    print("To [Q]uit - press letter - Q")
    task = input("What do you want to do? (C / D / S / I / O / R / Q)? ")
    print("")


    # Creating the new task in Windows Task Scheduler
    if task == "c" or task == "C":
        while True:
            time_input = input("Enter the time in the format 'HH:MM': ")
            try:
                time = datetime.strptime(time_input, '%H:%M').time()
                break
            except ValueError:
                print("Error: Invalid time format. Please try again.")
  
        
        file_name = "start_process.py"
        program = "schtasks"
        start_in = MAIN_DIRECTORY
        arguments = ['/create', '/tn', task_name, '/tr', f'cmd /c cd /d "{start_in}" & "{sys.executable}" "{file_name}"', '/sc', 'daily', '/st', time.strftime('%H:%M')]
        return_code = subprocess.call([program] + arguments, shell=True)

        if return_code == 0:
            print("Task was successful created! \n")
            return function_task()
        else:
            text = "ERROR during installation. Return code: " + str(return_code) + "\n"
            with open(LOGS_ERR_PATH, "a") as file:
                file.write(text)
            print(text, return_code)
            return function_task()


    # Delete previously created task
    elif task == "d" or task == "D":
        return_code = subprocess.call(['schtasks', '/delete', '/tn', task_name, '/f'])
        if return_code == 0:
            print("Task was successfully deleted. \n")
            return function_task()
        else:
            text = "ERROR: Task was not deleted. Most likely it wasn't created before. Error return code: " + str(return_code) + "\n"
            with open(LOGS_ERR_PATH, "a") as file:
                file.write(text)
            print(text)
            return function_task()


    # Will send birthday reminding letters right now
    elif task == "s" or task == "S":
        import start_process
        return function_task()


    # Change e-mail server information
    elif task == "i" or task == "I":
        create_login_file()
        return function_task()


    # Opens logs_and_errors file using Notepad
    elif task == "o" or task == "O":
        try:
            subprocess.Popen(['notepad.exe', LOGS_ERR_PATH])
            print("logs_and_errors.txt file was opened! \n")
            return function_task()
        except:
            print("logs_and_errors.txt file does not exist")
            return function_task()


    # Deletes logs_and_errors file
    elif task == "e" or task == "E":

        logs_file_dir = MAIN_DIRECTORY + "\\" + LOGS_ERR_PATH
        #print(logs_file_dir, "\n")
        
        if os.path.exists(logs_file_dir):
            os.remove(logs_file_dir)
            print("logs_and_errors file deleted successfully. \n")
            return function_task()
        else:
            print("logs_and_errors file does not exist. \n")
            return function_task()
        

    # Instruction how to manually create a daily task in Windows Task Scheduler 
    elif task == "r" or task == "R":
        print("In case you would like to create Windows Task Scheduler task manually please follow the instruction! \n")
        print("Go to the start menu and search for \"Task Scheduler\". Then open it.")
        print("In the upper left corner select \"Action\" and \"Create Task\".")
        print("In the \"General\" segment write the name of the task. It doesn't matter how you will call it.")
        print("In the \"Triggers\" segment push \"New\" and select the time and how often you would like the App would remind about birthdays.")
        print("In the \"Actions\" segment push \"New\" and then:")
        print("In the \"Program/script\" line write: ", sys.executable)
        print("In the \"Add arguments\" line write: check_errors.py")
        print("In the \"Start in\" line write: ", MAIN_DIRECTORY)
        print("")
        return function_task()


    # Quit the program
    elif task == "q" or task == "Q":
        sys.exit(0)


    # If a user selected a wrong symbol
    else:
        print("You have selected wrong letters, please try again! \n")
        return function_task()


def interface():
    intro()
    function_task()
interface()
