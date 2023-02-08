import automator
import vehicle
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper(automator.Automator):
    Automator = automator.Automator()
    website_url = "https://www.carvana.com/vehicle/2543527"
    website_urls = []
    vehicles = []
    
    def feed_urls(self):
        self.Automator.get_vehicle_urls()
        self.website_urls = self.Automator.urls
        for url in self.website_urls:
            self.scrape_no_vin_info(url)

    def scrape_no_vin_info(self, url):
        browser = webdriver.Chrome()
        browser.maximize_window() # For maximizing window
        browser.implicitly_wait(20) # gives an implicit wait for 20 seconds
        browser.get(url)
        browser.execute_script("window.scrollTo(0, 2194)") 
        elem = browser.find_element(By.XPATH,'//a[contains(@href,"/VehicleHistory/")]')
        # print(elem.location)
        vin_history_url = elem.get_attribute("href")
        browser.execute_script("window.scrollTo(0, 6177)") 
        elem1 = browser.find_element(By.ID,'inspection-150-point')
        elems = elem1.find_elements(By.TAG_NAME, 'p')
        text = elems[1].text
        words = text.split()
        year = words[1]
        company = words[2]
        model = words[3]
        self.vehicles.append(vehicle.Vehicle(year, company, model, vin_history_url))

Scraper = Scraper()
Scraper.feed_urls()
for vehicle in Scraper.vehicles:
    print("year: " + vehicle.year)
    print("company: "+ vehicle.company)
    print("model: "+ vehicle.model)
    print("vin history url: " + vehicle.vin_history_url)