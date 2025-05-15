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

app = Flask(__name__)
response = requests.get("https://api.fbi.gov/wanted/v1/list")
data = response.json()
print(data)
@app.route("/")




if __name__ == '__main__':
    app.run(debug=True)
print(data['total'])
print(data['items'][0]['title'])
"""