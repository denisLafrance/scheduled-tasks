# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import dt
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# get the birthday data from the data file
data = pandas.read_csv("birthdays.csv")
data = data.to_dict("records")

#get the current data
now = dt.datetime.now()

current_month = now.month
current_day = now.day

# Loop through the CSV file and pull out the records
for item in data:
    day = item["day"]
    month = item["month"]
    name = item["name"]
    email = item["email"]

    if current_month == month and current_day == day:
        print("yes today is your birthday")

        #Get all the data from the letter file
        with open("letter.txt", "r") as letter:
            letter_data = letter.read()
            updated_data = letter_data.replace("[NAME]", name)

        # This will send the email to the user
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{email}",
                msg=f"Subject: Happy birthday {name}\n\n{updated_data}"
            )

