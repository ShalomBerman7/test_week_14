import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password"
)
cursor = conn.cursor()

cursor.execute("""CREATE DATABASE IF NOT EXISTS Weapons""")
conn.commit()

cursor.execute("""USE Weapons""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Teacher(
               id INT PRIMARY KEY,
               weapon_id VARCHAR(255)),
               weapon_name VARCHAR(255)),
               weapon_type VARCHAR(255),
               range_km INT,
               weight_kg FLOAT,
               manufacturer VARCHAR(255),
               origin_country VARCHAR(255),
               storage_location VARCHAR(255),
               year_estimated INT,
               level_risk VARCHAR(255),
               """)
conn.commit()
