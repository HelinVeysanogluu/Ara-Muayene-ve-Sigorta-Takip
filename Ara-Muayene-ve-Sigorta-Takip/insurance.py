from dataclasses import dataclass
from datetime import date
from vehicle import Vehicle
from typing import Optional

@dataclass
class Insurance:
    def __init__(
        self,
        vehicle: Vehicle,
        insurance_type: str,
        insurance_company: str,
        policy_number: str,
        policy_amount: float,
        start_date: date,
        end_date: date,
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
            f"Sigorta Türü : {self.insurance_type}\n"
            f"Şirket          : {self.insurance_company}\n"
            f"Poliçe No     : {self.policy_number}\n"
            f"Tutar           : {self.policy_amount:.2f} TL\n"
            f"Başlangıç     : {self.start_date.strftime('%d.%m.%Y')}\n"
            f"Bitiş           : {self.end_date.strftime('%d.%m.%Y')}\n"
            f"Durum          : {self.status}"
        )

from vehicle import vehicles

insurances = [
    Insurance(
        vehicle=vehicles[0],
        insurance_type="Kasko",
        insurance_company="Sigorta",
        policy_number="ABC123456",
        policy_amount=2300.00,
        start_date=date(2025, 7, 1),
        end_date=date(2026, 7, 1),
        status="Aktif"
    )
]