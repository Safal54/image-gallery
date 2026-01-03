import requests
import smtplib
import os
from twilio.rest import Client


OWM_endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key ="#"
account_sid="#"
auth_token="#"
client=Client(account_sid, auth_token)

paramitars= {
    "lat":35.937496,
    "lon":14.375416,
    "cnt":4,
    "appid":api_key

}

response= requests.get(OWM_endpoint,params=paramitars)
response.raise_for_status()
data= response.json()
weather_data=data["list"]

is_raining= False
for weather_hour in weather_data:
    weather_code= weather_hour["weather"][0]["id"]
    if weather_code <700:
        is_raining= True

if is_raining:
    message = client.messages.create(
        body="Seems like it will be raining today don't forget to take a umbrella Safal😊😊💕",
        from_="+17656978594",
        to="+35699797636",

    )
    print(message.status)



#
# def today_weather():
#     if today<700:
#         msg=f"Subject:Weather forecast\n    The weather of today seems need of umbrella.todays weather code is  {today} "
#         return msg
#     else:
#         msg=f"Subject:Weather forecast\n    The weather of today is good  enough as usual .todays weather code is {today} "
#         return msg
#
# response= smtplib.SMTP("smtp.gmail.com",port=587)
# response.starttls()
# response.login(user="safalbohora2000@gmail.com",password="mcwpwhznzyomvxkb")
# response.sendmail(from_addr="safalbohora2000@gmail.com",to_addrs="safal.bohora@icloud.com",
#                   msg=today_weather())
#





