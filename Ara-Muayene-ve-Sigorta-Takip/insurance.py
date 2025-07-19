from datetime import date
from typing import Optional
from vehicle import Vehicle


class Insurance:
    def __init__(
        self,
        vehicle: Vehicle,
        insurance_type: str,
        insurance_company: str,
        policy_number: str,
        policy_amount: float,
        start_date: date,
        end_date: Optional[date],
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
        lines = [
            f"Plaka           : {self.vehicle.license_plate}",
            f"Sigorta Türü    : {self.insurance_type}",
            f"Sigorta Şirketi : {self.insurance_company}",
            f"Poliçe No       : {self.policy_number}",
            f"Poliçe Tutarı   : {self.policy_amount:.2f} TL",
            f"Başlangıç Tarihi: {self.start_date.strftime('%d.%m.%Y')}",
            f"Bitiş Tarihi    : {self.end_date.strftime('%d.%m.%Y')}" if self.end_date else "Bitiş Tarihi       : Belirtilmemiş",
            f"Durum           : {self.status}"
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    from vehicle import Brand, Model, Vehicle_Type, Vehicle

    brand = Brand(1, "Renault")
    vtype = Vehicle_Type(1, "Binek")
    model = Model(1, "Clio", brand)
    vehicle = Vehicle(202, "01HLN34", "Temizlik İşleri", brand, model, vtype, "Pasif")

    insurance = Insurance(
        vehicle=vehicle,
        insurance_type="Kasko",
        insurance_company="Şirket",
        policy_number="012abc345",
        policy_amount=2300.00,
        start_date=date(2025, 7, 1),
        end_date=date(2026, 7, 1),
        status="Aktif"
    )

    print(insurance)
