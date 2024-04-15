# Coffee-and-Wifi

The Cafe Finder is a Flask web application that allows users to add and view cafes, including details such as location, opening and closing times, coffee rating, wifi strength rating, and the number of power outlets available. Users can add new cafes and view existing cafes in a list format.

## Features

- **Add Cafe**: Users can add new cafes to the database by filling out a form with cafe details, including name, location, opening and closing times, coffee rating, wifi strength rating, and the number of power outlets.

- **View Cafes**: Users can view all existing cafes in a list format, displaying cafe details such as name, location, opening and closing times, coffee rating, wifi strength rating, and the number of power outlets.

## Setup

1. Install Dependencies: Run `pip install -r requirements.txt` to install all required packages.

2. Run the Application: Execute `python app.py` to start the Flask server. Visit `http://localhost:5000` in your web browser to view the application.

## Usage

- Navigate to `http://localhost:5000` in your web browser to access the homepage and explore the available features.

- To add a new cafe, click on the "Add Cafe" link and fill out the form with cafe details. Click the "Submit" button to add the cafe to the database.

- To view all existing cafes, click on the "View Cafes" link. The cafes will be displayed in a list format with details such as name, location, opening and closing times, coffee rating, wifi strength rating, and the number of power outlets.

## File Structure

- `app.py`: Main Flask application file containing route definitions and form configurations.

- `templates/`: Directory containing HTML templates for rendering web pages.

- `static/`: Directory containing static files such as CSS stylesheets and JavaScript files.

## Dependencies

- Flask
- Flask Bootstrap
- Flask WTF

All dependencies are listed in the `requirements.txt` file.

## Data Persistence

The cafe data is stored in a CSV file named `cafe-data.csv` located in the project directory. Each row in the CSV file represents a cafe entry with details such as name, location, opening and closing times, coffee rating, wifi strength rating, and the number of power outlets.

## Disclaimer

Ensure that you have the necessary permissions and abide by the terms of service of any services used in this project. The developer is not responsible for any misuse of this application.

