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
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/") #this is home page
def index():
    page = request.args.get("page", default=1, type=int)
    search = request.args.get("search", default="", type=str)
    status = request.args.get("status", default="", type=str)
    species = request.args.get("species", default="", type=str)
    gender = request.args.get("gender", default="", type=str)


    params = {"page": page}
    if search:
        params["name"] = search
    if status:
        params["status"] = status
    if species:
        params["species"] = species
    if gender:
        params["gender"] = gender

    response = requests.get("https://rickandmortyapi.com/api/character", params=params)
#if the the characters cannot be found js say not found
    if response.status_code == 404:
        return render_template("index.html",
            characters=[],
            current_page=page,
            total_pages=0,
            next_page=None,
            prev_page=None,
            error="No characters found.",
            request=request)

    data = response.json()
    characters = data["results"]
    total_pages = data["info"]["pages"]

    char_list = [{
        "id": char["id"],
        "name": char["name"],
        "image": char["image"],
        "species": char["species"],
        "status": char["status"]
    } for char in characters] #page change
    next_page = page + 1 if data["info"]["next"] else None
    prev_page = page - 1 if data["info"]["prev"] else None
    return render_template("index.html",
        characters=char_list,
        current_page=page,
        total_pages=total_pages,
        next_page=next_page,
        prev_page=prev_page,
        error=None,
        request=request)
#app route to display characters individually when u click on their card
@app.route("/character/<int:character_id>")
def character_detail(character_id):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
# if the status isn't 200, or if it doesn't work, then say character not found
    if response.status_code != 200:
        return render_template("character.html", character=None, error="Character not found.")

    data = response.json()

    character = {
        "id": data["id"],
        "name": data["name"],
        "image": data["image"],
        "species": data["species"],
        "status": data["status"],
        "gender": data["gender"],
        "origin": data["origin"]["name"],
        "location": data["location"]["name"]
    }

    return render_template("character.html", character=character, error=None)
if __name__ == "__main__":
    app.run(debug=True)

""" 
import requests

params = {
    "name": "rick",
    "species": "human",
    "status": "alive",
    "gender": "male"
}

response = requests.get("https://rickandmortyapi.com/api/character/", params=params)

if response.status_code == 200:
    data = response.json()
    for character in data["results"]:
        print(character["name"])
else:
    print("Error:", response.status_code)
 """