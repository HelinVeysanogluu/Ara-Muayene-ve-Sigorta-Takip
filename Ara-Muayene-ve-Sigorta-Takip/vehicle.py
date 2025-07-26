import psycopg2
from db import get_connection

class Vehicle:
    def __init__(self, vehicle_id, license_plate, assigned_unit, brand, model, vehicle_type, status):
        self.id = vehicle_id
        self.license_plate = license_plate
        self.assigned_unit = assigned_unit
        self.brand = brand
        self.model = model
        self.vehicle_type = vehicle_type
        self.status = status

    def __str__(self):
        return (
            f"ID       : {self.id}\n"
            f"Plaka    : {self.license_plate}\n"
            f"Birim    : {self.assigned_unit}\n"
            f"Marka    : {self.brand}\n"
            f"Model    : {self.model}\n"
            f"Araç Tipi: {self.vehicle_type}\n"
            f"Durum    : {self.status}"
        )

def get_vehicle_by_plate(plate):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT vehicle_id, license_plate, assigned_unit,
               brand, model, vehicle_type, status
        FROM vehicle
        WHERE REPLACE(UPPER(license_plate), ' ', '') = %s
    """, (plate.upper().replace(" ", ""),))

    row = cur.fetchone()
    conn.close()

    if row:
        return Vehicle(*row)
    return None
