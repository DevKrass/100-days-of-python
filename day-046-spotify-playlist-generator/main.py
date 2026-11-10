import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from ytmusicapi import YTMusic

load_dotenv()

date = input(
    "Which yeard do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
)

# App Brewery authentication
header = {"User-Agent": os.getenv("AUTH")}

response = requests.get(
    url=f"https://appbrewery.github.io/bakeboard-hot-100/{date}", headers=header
)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
songs = soup.find_all(name="h3", class_="chart-entry__title")
song_titles = [song.getText() for song in songs]

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")


playlist_name = f"{date} Billboard 100"


# Check if playlist already exists
playlist_id = None

for playlist in playlists:
    if playlist_name == playlist["title"]:
        print("Playlist name already exists")
        playlist_id = playlist["playlistId"]
        break

# Create playlist if it doesn't exist
if playlist_id is None:
    playlist_id = yt.create_playlist(
        title=playlist_name, description=f"Top songs from {date}"
    )
    print(f"Created playlist named: {playlist_name}")

    # Search and add songs
    for title in song_titles:
        try:
            search = yt.search(title, filter="songs", limit=1)
            yt.add_playlist_items(playlist_id, [search[0]["videoId"]])
            print(f"Added {title}")
        except Exception as e:
            print(f"Skipped: {title} | Reason: {e}")
