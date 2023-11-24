import sqlite3
from datetime import datetime, timedelta
from datetime import datetime
import pytz  # Asegúrate de tener esta línea


class DBStorage:
    def _init_(self, db_name="data.db"):
        self.db_name = db_name
        self.db = None
        self.cursor = None

    def connect(self):
        self.db = sqlite3.connect(self.db_name)
        self.cursor = self.db.cursor()

    def disconnect(self):
        self.db.close()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS mediciones (id INTEGER PRIMARY KEY AUTOINCREMENT, valor_temperatura FLOAT, valor_humedad FLOAT, valor_fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    def insert(self, humedad, temperatura):
        fecha = datetime.now()
        self.cursor.execute(
            "INSERT INTO mediciones (valor_humedad, valor_temperatura, valor_fecha) VALUES (?, ?, ?)", (humedad, temperatura,fecha))
        self.db.commit()

    def get_measurements(self):
        self.cursor.execute("SELECT * FROM mediciones")
        labels = []
        temperatures = []
        humidities = []

        for row in self.cursor.fetchall():
            labels.append(row[3])
            temperatures.append(row[1])
            humidities.append(row[2])
        return {
            "labels": labels,
            "temperatures": temperatures,
            "humidities": humidities
        }

    def get_measurements_last_hour(self):
        end = datetime.now()
        start = end - timedelta(hours=1)

        query = "SELECT * FROM mediciones WHERE valor_fecha >= ? AND valor_fecha <= ?"
        self.cursor.execute(query, (start, end))
        
        labels = []
        temperatures = []
        humidities = []

        for row in self.cursor.fetchall():
            labels.append(row[3])
            temperatures.append(row[1])
            humidities.append(row[2])

        return {
            "labels": labels,
            "temperatures": temperatures,
            "humidities": humidities
        }
    
    

if _name_ == "_main_":
    db = DBStorage("data.db")
    db.connect()
    db.create_table()
    db.insert(10, 20)

    print("All Measurements:")
    print(db.get_measurements())

    print("\nMeasurements from Last Hour:")
    print(db.get_measurements_last_hour())

    db.disconnect()