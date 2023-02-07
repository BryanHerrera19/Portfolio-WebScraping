class Vehicle():
    model = ''
    year = 0
    company = ''
    def __init__(self, year, company, model):
        self.model = model
        self.year = year
        self.company = company