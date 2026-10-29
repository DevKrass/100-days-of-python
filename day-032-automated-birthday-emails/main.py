##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import datetime as dt
import random
import smtplib

import pandas

MY_EMAIL = "your-email@gmail.com"
PASSWORD = "your password"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row for _, data_row in data.iterrows()
}
letter_templates = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt",
]

now = dt.datetime.now()
month = now.month
day = now.day

if (month, day) in birthdays_dict:
    random_letter = random.choice(letter_templates)
    name = birthdays_dict[(month, day)]["name"]
    email = birthdays_dict[(month, day)]["email"]
    with open(random_letter) as file:
        letter = file.read().replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject: Happy birthday {name}\n\n {letter}",
        )
