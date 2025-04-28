## How to Setup the Application

### Prerequisites
- Python 3.6 or higher
- MySQL Server
- pip (Python package installer)

1. Set up the database by running flight_tracking database set up sql file
2. Load the stored procedures and views onto the database by running the sql file with all stored procedures and views
3. Get the user and host login details and load them into config.py file so the backend can connect to the database
4. Clone this repository
5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Run the Application

1. Instructions for MySQL database stuff
2. Run the Flask application:
   ```
   python app.py
   ```
4. Open a web browser and navigate to: `http://localhost:5000`

## Technologies Used

### Backend
- **Flask**: A lightweight WSGI web application framework in Python
- **MySQL**: Relational database management system
- **mysql-connector-python**: Python driver for MySQL

### Frontend
- **HTML/CSS**: For building the user interface
- **JavaScript**: For interactive elements on the web pages


## Team Work Distribution

Our team of 4 members divided the work as follows:

- **Team Member 1**: blah blah
- **Joie Yeung**: Frontend HTML/CSS templates, UI design
- **Team Member 3**: blah blah
- **Team Member 4**: blah blah

All team members contributed to the overall application and collaborated on integrating the different components together.
