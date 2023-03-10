import csv
import smtplib
from constants import CONTACTS_PATH
from constants import LOGS_ERR_PATH
from constants import LOGIN_PATH
from functions import last_log
from check_data_for_birthdays import upcoming_birthdays

# Counting how many persons will have birthdays
upcoming_birthday_count = len(upcoming_birthdays)

i=0

# Function needed in case there would be more than 1 person with the birthday same day
while i < upcoming_birthday_count:
    
    # Reading csv file
    with open(CONTACTS_PATH, "r") as file:
            reader = csv.reader(file)
            header = next(reader)

            # Collecting information about birthday persons 
            for row in reader:
                name = row[0]
                email = row[1]
                birthdate = row[2]

                if name in upcoming_birthdays[i]:
                    name_of_birthday_person = name
                    date = birthdate
                    break

            # Collecting information about non birthday persons 
            file.seek(0)
            header = next(reader)
            for row in reader:
                name = row[0]
                email = row[1]

                # Sending letters 
                if name not in upcoming_birthdays[i]:

                    # Reading e-mail server information from login.csv
                    with open(LOGIN_PATH, "r") as file:
                        reader = csv.reader(file)
                        header = next(reader, None)
                        if header is None:
                            with open(LOGS_ERR_PATH, "a") as file:
                                file.write("No header row found in the login.csv file" + "\n")     
                            print("No header row found in the login.csv file")
                        else:

                            # Reading data
                            data = next(reader, None)
                            if data is None:
                                with open(LOGS_ERR_PATH, "a") as file:
                                    file.write("No data found in the login.csv file" + "\n")
                                print("No data found in the CSV file")
                            else:

                                # Assigning the values from the data row to the variables
                                login = data[0]
                                password = data[1]
                                host = data[2]
                                port = data[3]
                                sender_email = data[4]
                            
                                j = 0

                                # Trying 3 times to send the letters and collecting errors if such occurs
                                while j < 3:
                                    try:
                                        server = smtplib.SMTP(host, port)
                                        server.ehlo()
                                        server.starttls()
                                        server.login(login, password)
                                        recipient_email = email
                                        subject = f"Birthday Reminder: {name_of_birthday_person} birthday on {date}"
                                        message = f"Hi {name},\n\n This is a reminder that {name_of_birthday_person} will be celebrating their birthday on {date}.\n\n There are 7 days left to get a present! \n"
                                        email_text = f"Subject: {subject}\n\n{message}"
                                        server.sendmail(sender_email, recipient_email, email_text)
                                        with open(LOGS_ERR_PATH, "a") as file:
                                            file.write(f"Email successfully sent to {name}!" + "\n")
                                        print(f"Email successfully sent to {name}!")
                                        server.quit()
                                        break
                                    
                                    # Handling exceptions and writing those to log file
                                    except Exception as e:
                                        print(f"Attempt No. {j+1} to send mail to {name} failed: {e}")
                                        with open(LOGS_ERR_PATH, "a") as file:
                                            file.write(f"Attempt No. {j+1} to send mail to {name} failed: {e}" + "\n")
                                        j+=1
                                        continue
                                else:
                                    with open(LOGS_ERR_PATH, "a") as file:
                                        file.write(f"All 3 attempts to send the email to {name} have failed." + "\n")
                                    print(f"All 3 attempts to send the email to {name} have failed.")                            

    print("")
    file.close()
    i+=1

# Function that writes the time the program finished the work
last_log()
