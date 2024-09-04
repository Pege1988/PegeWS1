from configparser import ConfigParser
import json
import sqlite3
from urllib.request import urlopen

config = ConfigParser()
config.read('config.ini')

def log_connection(status_code, message, database):
    """Log the HTTP connection status to the database."""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO connection_log (status_code, message) VALUES (?, ?)', (status_code, message))
    conn.commit()
    conn.close()

def read_json(url, database):
    try:
        json_url = urlopen(url).read()
        print("Request url successfully opened.")
        log_connection(200, "Request url successfully opened.", database)
        return(json_url)
    except Exception as e:
        # Log read failure
        log_connection(500, str(e), database)
        print(f"Error opening request url: {e}")

# Script to get JSON file for real time weather data
def get_data(json_file, database):
    try:
        data = json.loads(json_file)
        print("Data read successfully from file.")
        log_connection(200, "Data read successfully from file.", database)
        return(data)
    except Exception as e:
        # Log read failure
        log_connection(500, str(e), database)
        print(f"Error reading data from file: {e}")