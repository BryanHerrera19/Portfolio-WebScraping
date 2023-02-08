class Vehicle():
    url = ''
    model = ''
    year = 0
    company = ''
    vin = ''
    vin_history_url = ''
    image = ''
    def __init__(self, url, year, company, model, vin_history_url, image):
        self.model = model
        self.year = year
        self.company = company
        self.vin_history_url = vin_history_url
        self.image = image
        self.url = url