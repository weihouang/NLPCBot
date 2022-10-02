from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
@app.route("/newend")
def a():
    return  "Hey it's Jake from StateFarm!"+'\n'+ "Which Insurance would you like to learn about? (Renter, Hospital Income, Medical Supplement Income, Pet)"

        