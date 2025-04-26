from flask import Flask, render_template, request
from db.db import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_airplane', methods=['GET', 'POST'])
def add_airplane_page():
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
        return render_template("add_airplane.html", reason=reason)
    else:
        return render_template("add_airplane.html")

@app.route('/add_airport', methods=['GET', 'POST'])
def add_airport_page():
    if request.method == 'POST':
        airportID = request.form["airportID"]
        name = request.form["name"]
        city = request.form["city"]
        state = request.form["state"]
        country = request.form["country"]
        locID = request.form["locID"]
        status, reason = add_airport(airportID, name, city, state, country, locID)
        print(reason)
        return render_template("add_airport.html", reason=reason)
    else:
        return render_template("add_airport.html")

@app.route('/add_person', methods=['GET', 'POST'])
def add_person_page():
    if request.method == 'POST':
        personID = request.form["personID"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        locID = request.form["locID"]
        taxID = request.form["taxID"]
        exp = request.form["exp"]
        miles = request.form["miles"]
        funds = request.form["funds"]
        status, reason = add_person(personID, fname, lname, locID, taxID, exp, miles, funds)
        print(reason)
        return render_template("add_person.html", reason=reason)
    else:
        return render_template("add_person.html")

@app.route('/grant_revoke_license', methods=['GET', 'POST'])
def grant_revoke_license_page():
    if request.method == 'POST':
        personID = request.form["personID"]
        license = request.form["license"]
        status, reason = grant_or_revoke_pilot_license(personID, license)
        print(reason)
        return render_template("grant_revoke_license.html", reason=reason)
    else:
        return render_template("grant_revoke_license.html")

@app.route('/offer_flight', methods=['GET', 'POST'])
def offer_flight_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        routeID = request.form["routeID"]
        airline = request.form["airline"]
        tail = request.form["tail"]
        progress = request.form["progress"]
        nexttime = request.form["nexttime"]
        cost = request.form["cost"]
        status, reason = offer_flight(flightID, routeID, airline, tail, progress, nexttime, cost)
        print(reason)
        return render_template("offer_flight.html", reason=reason)
    else:
        return render_template("offer_flight.html")

@app.route('/flight_landing', methods=['GET', 'POST'])
def flight_landing_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        status, reason = flight_landing(flightID)
        print(reason)
        return render_template("flight_landing.html", reason=reason)
    else:
        return render_template("flight_landing.html")

@app.route('/flight_takeoff', methods=['GET', 'POST'])
def flight_takeoff_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        status, reason = flight_takeoff(flightID)
        print(reason)
        return render_template("flight_takeoff.html", reason=reason)
    else:
        return render_template("flight_takeoff.html")

@app.route('/passengers_board', methods=['GET', 'POST'])
def passengers_board_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        status, reason = passengers_board(flightID)
        print(reason)
        return render_template("passengers_board.html", reason=reason)
    else:
        return render_template("passengers_board.html")

@app.route('/passengers_disembark', methods=['GET', 'POST'])
def passengers_disembark_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        status, reason = passengers_disembark(flightID)
        print(reason)
        return render_template("passengers_disembark.html", reason=reason)
    else:
        return render_template("passengers_disembark.html")

@app.route('/assign_pilot', methods=['GET', 'POST'])
def assign_pilot_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        personID = request.form["personID"]
        status, reason = assign_pilot(flightID, personID)
        print(reason)
        return render_template("assign_pilot.html", reason=reason)
    else:
        return render_template("assign_pilot.html")

@app.route('/recycle_crew', methods=['GET', 'POST'])
def recycle_crew_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        status, reason = recycle_crew(flightID)
        print(reason)
        return render_template("recycle_crew.html", reason=reason)
    else:
        return render_template("recycle_crew.html")

@app.route('/retire_flight', methods=['GET', 'POST'])
def retire_flight_page():
    if request.method == 'POST':
        flightID = request.form["flightID"]
        status, reason = retire_flight(flightID)
        print(reason)
        return render_template("retire_flight.html", reason=reason)
    else:
        return render_template("retire_flight.html")

@app.route('/simulation_cycle', methods=['GET', 'POST'])
def simulation_cycle_page():
    if request.method == 'POST':
        status, reason = simulation_cycle()
        print(reason)
        return render_template("simulation_cycle.html", reason=reason)
    else:
        return render_template("simulation_cycle.html")

@app.route('/flights_in_the_air', methods=['GET'])
def flights_in_the_air_page():
    data = get_flights_in_the_air()
    return render_template("flights_in_the_air.html", data=data)

@app.route('/flights_on_the_ground', methods=['GET'])
def flights_on_the_ground_page():
    data = get_flights_on_the_ground()
    return render_template("flights_on_the_ground.html", data=data)

@app.route('/people_in_the_air', methods=['GET'])
def people_in_the_air_page():
    data = get_people_in_the_air()
    return render_template("people_in_the_air.html", data=data)

@app.route('/people_on_the_ground', methods=['GET'])
def people_on_the_ground_page():
    data = get_people_on_the_ground()
    return render_template("people_on_the_ground.html", data=data)

@app.route('/route_summary', methods=['GET'])
def route_summary_page():
    data = get_route_summary()
    return render_template("route_summary.html", data=data)

@app.route('/alternative_airports', methods=['GET'])
def alternative_airports_page():
    data = get_alternative_airports()
    return render_template("alternative_airports.html", data=data)

@app.route('/choose-table', methods=['POST'])
def showdb():  # put application's code here
    if request.method == 'POST':
        tablename = request.form['tablename']
    return return_table(tablename)

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
