import psycopg2
from datetime import datetime
from vehicle import Vehicle, get_vehicle_by_plate
from typing import Optional, List
from db import get_connection

class Inspection:
    def __init__(
        self,
        vehicle: Vehicle,
        inspection_type: str,
        inspection_date: datetime,
        inspection_location: str,
        inspection_fee: float,
        result: str,
        inspection_personnel: str,
        next_inspection_date: Optional[datetime] = None,
        penalty: Optional[float] = None,
        description: Optional[str] = None,
    ):
        self.vehicle = vehicle
        self.inspection_type = inspection_type
        self.inspection_date = inspection_date
        self.inspection_location = inspection_location
        self.inspection_fee = inspection_fee
        self.penalty = penalty
        self.result = result
        self.next_inspection_date = next_inspection_date
        self.inspection_personnel = inspection_personnel
        self.description = description

    def __str__(self):
        lines = [
            f"Muayene Türü      : {self.inspection_type}",
            f"Muayene Tarihi    : {self.inspection_date.strftime('%d.%m.%Y')}",
            f"Ücret             : {self.inspection_fee:.2f} TL",
        ]

        if self.penalty:
            lines.append(f"Ceza              : {self.penalty:.2f} TL")

        lines += [
            f"Sonuç             : {self.result}",
            f"Sonraki Muayene   : {self.next_inspection_date.strftime('%d.%m.%Y')}" if self.next_inspection_date else "Sonraki Muayene   : Belirtilmemiş",
            f"Personel          : {self.inspection_personnel}",
            f"Açıklama          : {self.description if self.description else 'Yok'}"
        ]

        return "\n".join(lines)

def get_all_inspections_by_plate(plate) -> List[Inspection]:
    vehicle = get_vehicle_by_plate(plate)
    if not vehicle:
        return []

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT inspection_type, inspection_date, inspection_location,
               inspection_fee, result, inspection_personnel,
               next_inspection_date, penalty, description
        FROM inspection
        WHERE vehicle = %s
        ORDER BY inspection_date DESC
    """, (vehicle.id,))

    rows = cur.fetchall()
    conn.close()

    inspections = []
    for row in rows:
        inspection_date = datetime.strptime(row[1], '%d-%m-%Y')
        next_inspection_date = datetime.strptime(row[6], '%d-%m-%Y') if row[6] else None

        inspections.append(Inspection(
            vehicle,
            row[0], inspection_date, row[2], row[3],
            row[4], row[5], next_inspection_date, row[7], row[8]
        ))

    return inspections