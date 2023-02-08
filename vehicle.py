class Vehicle():
    model = ''
    year = 0
    company = ''
    vin = ''
    vin_history_url = ''
    def __init__(self, year, company, model, vin_history_url):
        self.model = model
        self.year = year
        self.company = company
        self.vin_history_url = vin_history_url