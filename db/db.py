import mysql.connector
from flask import render_template

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )
def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        return conn, cursor
    except Exception as e:
        print(f"DB Error: {str(e)}")
        return 0, 0

def close_connection(conn, cursor):
    cursor.close()
    conn.close()

def return_table(tablename):
    conn, cursor = test_connection()
    cursor.execute("Select * from {tablename}".format(tablename=tablename))
    results = cursor.fetchall()
    close_connection(conn, cursor)
    return render_template('home.html', table = results)

def fetchresponse(conn, cursor):
    result = next(cursor.stored_results()).fetchone()
    print("debug" + str(result))
    status = result['status_']
    reason = result['reason']
    conn.commit()
    close_connection(conn, cursor)
    return status, reason

def add_airplane(airplaneID, tailnum, seatcap, speed, locID, type, maintenanced, model, neo):
    if airplaneID == "" or tailnum == "" or seatcap == "" or speed == "" or locID == "" or type == "":
        return 0, "null vals"
    conn, cursor = test_connection()
    if maintenanced == "NULL" or maintenanced is None or maintenanced == "":
        maintenanced = None
    else:
        maintenanced = str(maintenanced)
    if model == "NULL" or model is None or model == "":
        model = None
    else:
        model = str(model)
    if neo == "NULL" or neo is None or neo == "":
        neo = None
    else:
        neo = 1 if (neo == "True" or neo == True) else 0

    try:
        cursor.callproc('add_airplane',
                   [(str(airplaneID)), (str(tailnum)),(str(seatcap)), (str(speed)), (str(locID)),
                   (str(type)), maintenanced, model, neo])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")

    return fetchresponse(conn, cursor)
'''
    result = next(cursor.stored_results()).fetchone()
    print("debug" + str(result))
    status = result['status_']
    reason = result['reason']
    conn.commit()
    close_connection(conn, cursor)
'''

def add_airport(airportID, name, city, state, country, locID):
    if airportID == "" or name == "" or city == "" or state == "" or country == "" or locID == "":
        return 0, "null vals"
    if (airportID.lower() == "null" or name.lower() == "null" or city.lower() == "null"
            or state.lower() == "null" or country.lower() == "null" or locID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('add_airport',
                   [(str(airportID)), (str(name)),(str(city)), (str(state)), (str(country)),
                   (str(locID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)


def add_person(personID, fname, lname, locID, taxID, exp, miles, funds):
    if personID == "" or fname == "" or lname == "" or locID == "":
        return 0, "null vals"
    if (personID.lower() == "null" or fname.lower() == "null" or lname.lower() == "null"
            or locID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    if taxID == "NULL" or taxID is None or taxID == "":
        taxID = None
    else:
        taxID = str(taxID)
    if exp == "NULL" or exp is None or exp == "":
        exp = None
    else:
        exp = str(exp)
    if miles == "NULL" or miles is None or miles == "":
        miles = None
    else:
        miles = str(miles)
    if funds == "NULL" or funds is None or funds == "":
        funds = None
    else:
        funds = str(funds)
    try:
        cursor.callproc('add_person',
                   [(str(personID)), (str(fname)),(str(lname)), (str(locID)), taxID, exp, miles, funds])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def grant_or_revoke_pilot_license(personID, license):
    if personID == "" or license == "":
        return 0, "null vals"
    if personID.lower() == "null" or license.lower() == "null":
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('grant_or_revoke_pilot_license',
                   [(str(personID)), (str(license))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def offer_flight(flightID, routeID, airline, tail, progress, nexttime, cost):
    if (flightID == "" or routeID == "" or airline == "" or tail == "" or progress == "" or
            nexttime == "" or cost == ""):
        return 0, "null vals"
    if (flightID.lower() == "null" or routeID.lower() == "null" or airline.lower() == "null" or
        tail.lower() == "null" or progress.lower() == "null" or nexttime.lower() == "null" or
        cost.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('offer_flight',
                   [(str(flightID)), (str(routeID)), (str(airline)), (str(tail)), (str(progress))
                    , (str(nexttime)), (str(cost))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def flight_landing(flightID):
    if (flightID == "" or flightID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('flight_landing',
                   [(str(flightID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def flight_takeoff(flightID):
    if (flightID == "" or flightID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('flight_takeoff',
                   [(str(flightID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def passengers_board(flightID):
    if (flightID == "" or flightID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('passengers_board',
                   [(str(flightID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def passengers_disembark(flightID):
    if (flightID == "" or flightID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('passengers_disembark',
                   [(str(flightID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def assign_pilot(flightID, personID):
    if (flightID == "" or flightID.lower() == "null" or personID == "" or personID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('assign_pilot',
                   [(str(flightID)), (str(personID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def recycle_crew(flightID):
    if (flightID == "" or flightID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('recycle_crew',
                   [(str(flightID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def retire_flight(flightID):
    if (flightID == "" or flightID.lower() == "null"):
        return 0, "null vals"
    conn, cursor = test_connection()
    try:
        cursor.callproc('retire_flight',
                   [(str(flightID))])
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def simulation_cycle():
    conn, cursor = test_connection()
    try:
        cursor.callproc('simulation_cycle')
    except Exception as e:
        print("hi")
        return 0, (f"Error: {str(e)}")
    return fetchresponse(conn, cursor)

def get_flights_in_the_air():
    conn, cursor = test_connection()
    try:
        cursor.execute("SELECT * FROM flights_in_the_air")
        results = cursor.fetchall()
        close_connection(conn, cursor)
        return results
    except Exception as e:
        print("Error retrieving flights_in_the_air:", e)
        close_connection(conn, cursor)
        return []

def get_flights_on_the_ground():
    conn, cursor = test_connection()
    try:
        cursor.execute("SELECT * FROM flights_on_the_ground")
        results = cursor.fetchall()
        close_connection(conn, cursor)
        return results
    except Exception as e:
        print("Error retrieving flights_on_the_ground:", e)
        close_connection(conn, cursor)
        return []

def get_people_in_the_air():
    conn, cursor = test_connection()
    try:
        cursor.execute("SELECT * FROM people_in_the_air")
        results = cursor.fetchall()
        close_connection(conn, cursor)
        return results
    except Exception as e:
        print("Error retrieving people_in_the_air:", e)
        close_connection(conn, cursor)
        return []

def get_people_on_the_ground():
    conn, cursor = test_connection()
    try:
        cursor.execute("SELECT * FROM people_on_the_ground")
        results = cursor.fetchall()
        close_connection(conn, cursor)
        return results
    except Exception as e:
        print("Error retrieving people_on_the_ground:", e)
        close_connection(conn, cursor)
        return []

def get_route_summary():
    conn, cursor = test_connection()
    try:
        cursor.execute("SELECT * FROM route_summary")
        results = cursor.fetchall()
        close_connection(conn, cursor)
        return results
    except Exception as e:
        print("Error retrieving route_summary:", e)
        close_connection(conn, cursor)
        return []

def get_alternative_airports():
    conn, cursor = test_connection()
    try:
        cursor.execute("SELECT * FROM alternative_airports")
        results = cursor.fetchall()
        close_connection(conn, cursor)
        return results
    except Exception as e:
        print("Error retrieving alternative_airports:", e)
        close_connection(conn, cursor)
        return []





