from typing import Optional

class Brand:
    def __init__(self, brand_id: int, name: str):
        self.brand_id = brand_id
        self.name = name

    def __str__(self):
        return f"{self.name} (ID: {self.brand_id})"


class Model:
    def __init__(self, model_id: int, name: str, brand: Brand):
        self.model_id = model_id
        self.name = name
        self.brand = brand

    def __str__(self):
        return f"{self.brand.name} {self.name} (Model ID: {self.model_id})"


class Vehicle_Type:
    def __init__(self, type_id: int, name: str):
        self.type_id = type_id
        self.name = name

    def __str__(self):
        return f"{self.name} (Type ID: {self.type_id})"


class Vehicle:
    def __init__(self, vehicle_id: int, license_plate: str, assigned_unit: str, brand: Brand, model: Model, vehicle_type: Vehicle_Type, status: str):
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
            f"Marka    : {self.brand.name}\n"
            f"Model    : {self.model.name}\n"
            f"Araç Tipi: {self.vehicle_type.name}\n"
            f"Durum    : {self.status}"
        )


from vehicle import Brand, Model, Vehicle_Type, Vehicle

if __name__ == "__main__":
    brand = Brand(1, "Opel")
    vehicle_type = Vehicle_Type(1, "Binek")
    model = Model(1, "Astra", brand)
    vehicle = Vehicle(101, "01HLN34", "Makine İkmal", brand, model, vehicle_type, "Aktif")
    print(vehicle)