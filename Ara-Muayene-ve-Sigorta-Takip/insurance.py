import psycopg2
from datetime import datetime
from vehicle import Vehicle, get_vehicle_by_plate
from db import get_connection

class Insurance:
    def __init__(
        self,
        vehicle: Vehicle,
        insurance_type: str,
        insurance_company: str,
        policy_number: str,
        policy_amount: float,
        start_date: datetime,
        end_date: datetime,
        status: str
    ):
        self.vehicle = vehicle
        self.insurance_type = insurance_type
        self.insurance_company = insurance_company
        self.policy_number = policy_number
        self.policy_amount = policy_amount
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return (
            f"Plaka           : {self.vehicle.license_plate}\n"
            f"Sigorta Türü    : {self.insurance_type}\n"
            f"Şirket          : {self.insurance_company}\n"
            f"Poliçe No       : {self.policy_number}\n"
            f"Tutar           : {self.policy_amount:.2f} TL\n"
            f"Başlangıç       : {self.start_date.strftime('%d.%m.%Y')}\n"
            f"Bitiş           : {self.end_date.strftime('%d.%m.%Y')}\n"
            f"Durum           : {self.status}"
        )

def get_insurance_by_plate(plate):
    vehicle = get_vehicle_by_plate(plate)
    if not vehicle:
        return None

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT insurance_type, insurance_company, policy_number,
               policy_amount, start_date, end_date, status
        FROM insurance
        WHERE vehicle = %s
        ORDER BY start_date DESC
        LIMIT 1
    """, (vehicle.id,))

    row = cur.fetchone()
    conn.close()

    if row:
        start_date = datetime.strptime(row[4], '%d-%m-%Y')
        end_date = datetime.strptime(row[5], '%d-%m-%Y')

        return Insurance(
            vehicle,
            row[0], row[1], row[2], row[3],
            start_date, end_date, row[6]
        )
    return None