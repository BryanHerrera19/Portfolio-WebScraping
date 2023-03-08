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
    num_owners = 0
    accidents = False
    last_state = ''
    regular_oil_changes = False
    usage = ''

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

    def vin_history_setter(self, num_owners, accidents, last_state, regular_oil_changes, usage):
        self.num_owners = num_owners
        self.accidents = accidents
        self.last_state = last_state
        self.regular_oil_changes = regular_oil_changes
        self.usage = usage