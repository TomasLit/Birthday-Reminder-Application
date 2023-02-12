import csv
import smtplib
from check_data import upcoming_birthdays
from check_errors import data_file


upcoming_birthday_count = len(upcoming_birthdays)


i=0

while i < upcoming_birthday_count:
    
    # Reading csv file
    with open(data_file, 'r') as file:
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

                # Sending letters. 
                if name not in upcoming_birthdays[i]:
                    
                    sender_email = ""
                    password = ""

                    # Checked using development server at https://develmail.com/
                    sender_email = 'tomas@verslas.lt'
                    server = smtplib.SMTP('smtp.develmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(sender_email, password)

                    recipient_email = email
                    subject = f"Birthday Reminder: {name_of_birthday_person} birthday on {date}"
                    message = f"Hi {name},\n\n This is a reminder that {name_of_birthday_person} will be celebrating their birthday on {date}.\n\n There are 7 days left to get a present! \n"
                    email_text = f"Subject: {subject}\n\n{message}"
                    server.sendmail(sender_email, recipient_email, email_text)
                    print(f"Email sent to {name}!")
                    server.quit()

    file.close()
    i+=1
    print("i= ", i)