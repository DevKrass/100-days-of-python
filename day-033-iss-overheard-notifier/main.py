import smtplib
import time
from datetime import datetime

import requests

MY_LAT = 00.000000  # Your latitude
MY_LONG = -00.000000  # Your longitude

YOUR_EMAIL = "example-email@gmail.com"
YOUR_PASSWORD = "example-password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
while True:
    time.sleep(60)
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LONG + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        and (hour_now >= sunset or hour_now <= sunrise)
    ):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
            connection.send_message(
                "Subject: ISS overhead\n\n ISS is overhead look up!"
            )
