from flask import Flask, render_template, request
from db.db import *

app = Flask(__name__)


@app.route('/')
def showdb():  # put application's code here
    return return_table()

@app.route('/testing', methods =['GET', 'POST'])
def testing():
    if request.method == 'POST':
        airlineID = request.form["airlineID"]
        tailnum = request.form["tailnum"]
        seatcap = request.form["seatcap"]
        speed = request.form["speed"]
        locID = request.form["locID"]
        type = request.form["type"]
        maintained = request.form["maintained"]
        model = request.form["model"]
        neo = request.form["neo"]
        status, reason = add_airplane(airlineID, tailnum, seatcap, speed, locID, type, maintained, model, neo)
        print(reason)
        return render_template("home.html", reason = reason)



if __name__ == '__main__':
    app.run()
