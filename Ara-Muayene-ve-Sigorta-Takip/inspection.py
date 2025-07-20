from dataclasses import dataclass
from datetime import date
from vehicle import Vehicle
from typing import Optional

@dataclass
class Inspection:
    def __init__(
        self,
        vehicle: Vehicle,
        inspection_type: str,
        inspection_date: date,
        inspection_location: str,
        inspection_fee: float,
        result: str,
        inspection_personnel: str,
        next_inspection_date: Optional[date] = None,
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
            f"Plaka             : {self.vehicle.license_plate}",
            f"Muayene Türü   : {self.inspection_type}",
            f"Muayene Tarihi : {self.inspection_date.strftime('%d.%m.%Y')}",
            f"Ücret             : {self.inspection_fee:.2f} TL",
        ]

        if self.penalty:
            lines.append(f"Ceza           : {self.penalty:.2f} TL")

        lines += [
            f"Sonuç            : {self.result}",
            f"Sonraki Muayene: {self.next_inspection_date.strftime('%d.%m.%Y')}" if self.next_inspection_date else "Sonraki Muayene: Belirtilmemiş",
            f"Personel        : {self.inspection_personnel}",
            f"Açıklama        : {self.description if self.description else 'Yok'}"
        ]

        return "\n".join(lines)

from vehicle import vehicles

inspections = [
    Inspection(
        vehicle=vehicles[0],
        inspection_type="Fenni",
        inspection_date=date(2025, 7, 15),
        inspection_location="İstanbul",
        inspection_fee=450.0,
        result="Başarılı",
        inspection_personnel="Helin",
        next_inspection_date=date(2026, 7, 15),
        penalty=None,
        description="Sorunsuz geçti"
    )
]