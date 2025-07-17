class Vehicle:
    def __init__(self, id, license_plate, assigned_unit, brand_id, model_id, type_id, status):
        self.id = id
        self.license_plate = license_plate
        self.assigned_unit = assigned_unit
        self.brand_id = brand_id
        self.model_id = model_id
        self.type_id = type_id
        self.status = status

class Brand:
    def __init__(self, brand_id, name):
        self.brand_id = brand_id
        self.name = name

class Model:
    def __init__(self, model_id, name, brand_id):
        self.model_id = model_id
        self.name = name
        self.brand_id = brand_id

class Vehicle_Type:
    def __init__(self, type_id, name):
        self.type_id = type_id
        self.name = name