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
    color = ''
    fuel = ''
    def __init__(self, url, image, fuel):
        self.image = image
        self.url = url
        self.fuel = fuel
    
    def model_year_company_miles_price_setter(self, model, year, company, miles, price):
        self.model = model
        self.year = year
        self.company = company
        self.miles = miles
        self.price = price

    def transmission_color_vinHistoryURL_setter(self, transmission, color, vinHistoryURL):
        self.transmission_type = transmission
        self.color = color
        self.vin_history_url = vinHistoryURL