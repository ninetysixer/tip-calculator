import requests
from datetime import datetime
import smtplib
import time

my_email = ""  # your e-mail address
password = ""  # your app password

MY_LAT = 41.008240  # Your latitude
MY_LONG = 28.974800  # Your longitude


def position_checker():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if -5 <= MY_LAT - iss_latitude <= 5 and 5 >= MY_LONG - iss_longitude >= -5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True 


while True:
    time.sleep(60)
    if position_checker() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Look Up!\n\nYou can see the ISS!")
            
