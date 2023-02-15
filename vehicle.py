class Vehicle():
    url = ''
    model = ''
    year = 0
    company = ''
    vin = ''
    vin_history_url = ''
    image = ''
    miles = 0
    price = 0
    transmission_type = ''
    def __init__(self, url, year, company, model, vin_history_url, image, miles, price, transmission_type):
        self.model = model
        self.year = year
        self.company = company
        self.vin_history_url = vin_history_url
        self.image = image
        self.url = url
        self.miles = miles
        self.price = price
        self.transmission_type = transmission_type