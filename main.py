import datetime as dt
import pandas as pd
import random
import smtplib

my_email="safalbohora2000@gmail.com"
password="mcwpwhznzyomv"

#----making today's date touple----------
today_date=dt.datetime.now()
today_date_tuple=(today_date.month,today_date.day)

#---------making the dictionary with tuple as key and row as value
with open("birthday.csv")as data_file:
data= pd.read_csv(data_file)

birthday_dict={(row.month,row.day):row for (index,row) in data.iterrows()}

#--------------check if today date is in the birthday_dict------------
if today_date_tuple in birthday_dict.keys():
print("... we have the date that match today's date in the birthday_dict.")

with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as name_file:
content= name_file.read()
letter= content.replace("[NAME]",birthday_dict[today_date_tuple]["name"])

#----------email of reciver------------
email= birthday_dict[today_date_tuple]["email"]

#-------------send email now-----------
with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,
to_addrs=email,
msg=f"Subject:Birthday wish!\n\n{letter} "
)

print(f"The mail is send to {birthday_dict[today_date_tuple]["name"]} successfully.")

