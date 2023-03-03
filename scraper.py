from automator import Automator
import vehicle
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper(Automator):
    website_urls = []
    vehicles = []
    
    
    
    def feed_urls_imgs(self):
        self.automate_website()
        self.website_urls = self.urls
        images = self.images
        fuels = self.fuels
        for i, url in enumerate(self.website_urls):
            self.scrape_no_vin_info(url, images[i], fuels[i])


    def scrape_no_vin_info(self, url, image, fuel):
        newVehicle = vehicle.Vehicle(url, image, fuel)

        self.browser.get(url)
        self.browser.execute_script("window.scrollTo(0, 500)") 
        time.sleep(5)
        elems_p = self.browser.find_elements(By.TAG_NAME, 'p')
        elems_p_texts = []
        for elem in elems_p:
            elems_p_texts.append(elem.text)
        year_model_text = list(filter(lambda v: re.match('\d\d\d\d.*', v), elems_p_texts))[0]
        texts = year_model_text.split()
        year = int(texts[0])
        company = texts[1]
        model = texts[2]
        miles_text = list(filter(lambda v: re.match(r'.*\d+,\d+ Miles', v), elems_p_texts))[0]
        miles_text = re.findall('\d+,\d+', miles_text)[0]
        miles = int(miles_text.replace(',',''))
        price_text = list(filter(lambda v: re.match(r'\$\d+,\d+', v), elems_p_texts))[0]
        price = int(price_text.strip('$').replace(',',''))
        newVehicle.model_year_company_miles_price_setter(model, year, company, miles, price)

        # Basic information
        self.browser.execute_script("window.scrollTo(0, 2194)") 
        elems_li = self.browser.find_elements(By.CLASS_NAME, 'sc-4436f562-5')
        elems_li_texts = []
        for elem in elems_li:
            elems_li_texts.append(elem.text)
        if list(filter(lambda v: re.match(r'^Auto.*', v), elems_li_texts)) == []:
            if list(filter(lambda v: re.match(r'^Manual.*', v), elems_li_texts)) == []:
                if list(filter(lambda v: re.match(r'^CVT.*', v), elems_li_texts)) == []:
                    transmission_type = ''
                else:
                    transmission_type = 'CVT'
            else:
                transmission_type = 'Manual'
        else:
            transmission_type = 'Automatic'
        color_text = list(filter(lambda v: re.match(r'.* Exterior Color', v), elems_li_texts))[0]
        color = color_text.split()[0]
        elem_vin = self.browser.find_element(By.XPATH,'//a[contains(@href,"/VehicleHistory/")]')
        vin_history_url = elem_vin.get_attribute("href")
        newVehicle.transmission_color_vinHistoryURL_setter(transmission_type, color, vin_history_url)

        self.scrape_vin_info(vin_history_url)

        self.vehicles.append(newVehicle)

    def scrape_vin_info(self, vin_history_url):
        self.browser.get(vin_history_url)
#Can use dictionary function to simplify
#Format: newDict = dict(manufacturer = x, modelName = y, vin = z, color = a, year = b, currentMileage = c)
#Above can then be imported directly to DB

Scraper = Scraper()
Scraper.feed_urls_imgs()
for vehicle in Scraper.vehicles:
    print("vehicle url: " + vehicle.url)
    print("year: " + str(vehicle.year))
    print("company: "+ vehicle.company)
    print("model: "+ vehicle.model)
    print("vin history url: " + vehicle.vin_history_url)
    print("image url: " + vehicle.image)
    print("miles : " + str(vehicle.miles))
    print("price : " + str(vehicle.price))
    print("transmission type : " + vehicle.transmission_type)
    print("Exterior color: " + vehicle.color)
    print("fuel type: " + vehicle.fuel)