import mysql.connector
from datetime import datetime


class DatabaseHandler:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def insert_data(self, humidity, pressure, altitude, temperature):
        current_timestamp = datetime.now()

        sql = "INSERT INTO daten (Humidity, Pressure, Altitude, Temperature,time_stamp) VALUES (%s, %s, %s, %s, %s)"
        values = (humidity, pressure, altitude, temperature, current_timestamp)
        self.cursor.execute(sql, values)
        self.connection.commit()
        return self.cursor.rowcount

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
