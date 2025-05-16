""" API Project- You may choose any API that does not require OAuth.
-You must display data on page load as well as display data based on user input (this
can be interpreted many different ways).
-You must create multiple routes for this project.
-Use at least one example of selection (if/then or try/except)
-Use one example of iteration (For)
-Functions should be refactored for readability and testability
-You must have at least 1 route that contains a dynamic URL that changes the data
the user sees on the page.
-You may use more than one API to accomplish the project.
 """
from flask import Flask, render_template
import requests


mortys = []
base_url = "https://rickandmortyapi.com/api/character/"
page = 1

while True:
    response = requests.get(f"{base_url}?page={page}")
    data = response.json()
    
    # Filter characters with "Rick" in the name
    for character in data["results"]:
        if "morty" in character["name"].lower():
            mortys.append(character)
    
    # Go to the next page if available
    if data["info"]["next"]:
        page += 1
    else:
        break

# Print names of all "Rick" characters
for morty in mortys:
    print(morty["name"])
