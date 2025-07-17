from vehicle import Vehicle

class Insurance(Vehicle):
    def __init__(self, id, insurance_type, insurance_company, policy_number, policy_amount, start_date, end_date, status):
        super().__init__(id)
        self.insurance_type = insurance_type
        self.insurance_company = insurance_company
        self.policy_number = policy_number
        self.policy_amount = policy_amount
        self.start_date = start_date
        self.end_date = end_date
        self.status = status