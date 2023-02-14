# In this file I keep constants

import os

# Directory and name of data file e-mail server information will be saved 
LOGIN_PATH = "Data files/login.csv"

# Directory of the data file with the information about people
CONTACTS_PATH = "Data files/contacts.csv"

# Name of a file that holds all logs and errors
LOGS_ERR_PATH = "logs_and_errors.txt"

# Main directory of the program
MAIN_DIRECTORY = os.path.dirname(os.path.abspath(__file__))