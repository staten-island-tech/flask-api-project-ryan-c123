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

@app.route("/")
def index():
    # Step 1: Read page number from query string (default = 1)
    page = request.args.get("page", default=1, type=int)

    # Step 2: Get data from API
    response = requests.get("https://rickandmortyapi.com/api/character", params={"page": page})
    data = response.json()
    characters = data["results"]
    total_pages = data["info"]["pages"]

    # Step 3: Prepare character data
    char_list = []
    for char in characters:
        char_list.append({
            "id": char["id"],
            "name": char["name"],
            "image": char["image"],
            "species": char["species"],
            "status": char["status"]
        })

    # Step 4: Handle next and previous page numbers
    next_page = page + 1 if data["info"]["next"] else None
    prev_page = page - 1 if data["info"]["prev"] else None

    # Step 5: Pass everything to template
    return render_template("index.html", characters=char_list,
                           next_page=next_page,
                           prev_page=prev_page,
                           current_page=page,
                           total_pages=total_pages)
@app.route("/character/<int:id>")
def character_detail(id):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
    data = response.json()

    character = {
        "id": data["id"],
        "name": data["name"],
        "status": data["status"],
        "species": data["species"],
        "type": data["type"] if data["type"] else "Unknown",
        "gender": data["gender"],
        "origin": data["origin"]["name"],
        "location": data["location"]["name"],
        "image": data["image"]
    }

    return render_template("character.html", character=character)

if __name__ == '__main__':
    app.run(debug=True)
