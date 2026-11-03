import os
import requests
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

APPID = os.getenv("APPID")
APPKEY = os.getenv("APPKEY")

SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

nutrition_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheety_endpoint = SHEET_ENDPOINT

nutrition_headers = {
  "Content-Type": "application/json",
  "x-app-id": APPID,
  "x-app-key": APPKEY
}

weight = "Your weight"
height_cm = "your height"
age = "your age"
gender = "your gender"
exercise_description = input("Tell me which exercises you did: ")

nutrition_data = {
  "query": exercise_description,
  "weight": weight,
  "height_cm": height_cm,
  "age": age,
  "gender": gender  
}

response = requests.post(url=nutrition_endpoint, json=nutrition_data, headers=nutrition_headers)
result = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

sheety_header = {
  "Content-Type": "application/json",
  "Authorization": TOKEN
}

for exercise in result["exercises"]:
  sheety_data = {
    "workout": {
      "date": date,
      "time": time,
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
    } 
  }

  sheet_response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_header)

  print(sheet_response.text)