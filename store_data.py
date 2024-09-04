from datetime import datetime
import sqlite3

database = "PegeWS1.sqlite"

# get timestamp from time
def get_timestamp(data, l1, l2, l3="time"):
    ts = datetime.fromtimestamp(int(data["data"][l1][l2][l3]))
    return(ts)

# slicer
def slice_data(data, l1, l2, l3="value"):
    slice = data["data"][l1][l2][l3]
    return(slice)

# file status
def save_file_status(data, db):
    """Save file status data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO file_status (code, msg, time)
        VALUES (?, ?, ?)
        ''', (data['code'], data['msg'], datetime.fromtimestamp(int(data['time']))))
        conn.commit()
        print("File status stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close() 
    
def get_request_id(db):
    """Get request ID from file status data."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT request_id FROM file_status ORDER BY request_id DESC LIMIT 1
    ''')
    request_id = cursor.fetchone()[0]
    conn.close()
    return(request_id) 

def save_outdoor_data(data, db):
    """Save outdoor data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO outdoor (request_id, time, temperature, feels_like, app_temp, dew_point, humidity)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (get_request_id(db), get_timestamp(data, "outdoor", "temperature", "time"), slice_data(data, "outdoor", "temperature"), slice_data(data, "outdoor", "feels_like"), slice_data(data, "outdoor", "app_temp"), slice_data(data, "outdoor", "dew_point"), slice_data(data, "outdoor", "humidity")))
        conn.commit()
        print("Outdoor data stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close()

# indoor
def save_indoor_data(data, db):
    """Save indoor data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO indoor (request_id, time, temperature, humidity)
        VALUES (?, ?, ?, ?)
        ''', (get_request_id(db), get_timestamp(data, "indoor", "temperature", "time"), slice_data(data, "indoor", "temperature"), slice_data(data, "indoor", "humidity")))
        conn.commit()
        print("Indoor data stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close()


# pressure
def save_pressure_data(data, db):
    """Save pressure data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO pressure (request_id, time, absolute, relative)
        VALUES (?, ?, ?, ?)
        ''', (get_request_id(db), get_timestamp(data, "pressure", "absolute", "time"), slice_data(data, "pressure", "absolute"), slice_data(data, "pressure", "relative")))
        conn.commit()
        print("Pressure data stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close()

# solar_and_uvi
def save_solar_and_uvi_data(data, db):
    """Save solar_and_uvi data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO solar_and_uvi (request_id, time, absolute, relative)
        VALUES (?, ?, ?, ?)
        ''', (get_request_id(db), get_timestamp(data, "solar_and_uvi", "solar", "time"), slice_data(data, "solar_and_uvi", "solar"), slice_data(data, "solar_and_uvi", "uvi")))
        conn.commit() 
        print("Solar and uvi data stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close()

# wind
def save_wind_data(data, db):
    """Save wind data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO wind (request_id, time, wind_speed, wind_gust, wind_direction)
        VALUES (?, ?, ?, ?, ?)
        ''', (get_request_id(db), get_timestamp(data, "wind", "wind_speed", "time"), slice_data(data, "wind", "wind_speed"), slice_data(data, "wind", "wind_gust"), slice_data(data, "wind", "wind_direction")))
        conn.commit() 
        print("Wind data stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close()

# rainfall
def save_rainfall_data(data, db):
    """Save rainfall data to the database."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO rainfall (request_id, time, rain_rate, daily, event, hourly, weekly, monthly, yearly)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (get_request_id(db), get_timestamp(data, "rainfall", "rain_rate", "time"), slice_data(data, "rainfall", "rain_rate"), slice_data(data, "rainfall", "daily"), slice_data(data, "rainfall", "event"), slice_data(data, "rainfall", "hourly"), slice_data(data, "rainfall", "weekly"), slice_data(data, "rainfall", "monthly"), slice_data(data, "rainfall", "yearly")))
        conn.commit() 
        print("Rainfall data stored")
    except Exception as e:
        print(f"Data could not be stored: {e} missing")
    conn.close()