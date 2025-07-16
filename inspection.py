from vechile import Vehicle

class Inspection(Vehicle):
    def __init__(self, id, inspection_type, inspection_date, inspection_location, inspection_fee, penalty, result, next_inspection_date, inspection_personnel, description):
        super().__init__(id)
        self.inspection_type = inspection_type
        self.inspection_date = inspection_date
        self.inspection_location = inspection_location
        self.inspection_fee = inspection_fee
        self.penalty = penalty
        self.result = result
        self.next_inspection_date = next_inspection_date
        self.inspection_personnel = inspection_personnel
        self.description = description
