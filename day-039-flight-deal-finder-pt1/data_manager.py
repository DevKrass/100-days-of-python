import requests
import os
from dotenv import load_dotenv
import pprint
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEET_ENDPOINT")

class DataManager:
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._authorization = os.getenv("SHEET_AUTH_TOKEN")
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers={"Authorization": self._authorization})
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data    
    
    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            headers={"Authorization": self._authorization}
        )