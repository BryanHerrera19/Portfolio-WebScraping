import automator
import vehicle
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Scraper(automator.Automator):
    Automator = automator.Automator()
    website_url = "https://www.carvana.com/vehicle/2543527"
    website_urls = []
    vehicles = []
    browser = webdriver.Chrome()
    
    
    def feed_urls_imgs(self):
        self.Automator.get_vehicle_urls_imgs()
        self.website_urls = self.Automator.urls
        images = self.Automator.images
        for i, url in enumerate(self.website_urls):
            self.scrape_no_vin_info(url, images[i])


    def scrape_no_vin_info(self, url, image):
        browser = self.browser
        browser.maximize_window() # For maximizing window
        browser.implicitly_wait(10) # gives an implicit wait for 20 seconds

        browser.get(url)
        browser.execute_script("window.scrollTo(0, 500)") 
        time.sleep(5)
        elems_p = browser.find_elements(By.TAG_NAME, 'p')
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

        browser.execute_script("window.scrollTo(0, 2194)") 
        elems_li = browser.find_elements(By.CLASS_NAME, 'sc-4436f562-5')
        if(re.match(r'.*Electric.*',elems_li[0].text)):
            transmission_type = elems_li[6].text.split(',')[0]
        else:
            transmission_type = elems_li[5].text.split(',')[0]

        elem_vin = browser.find_element(By.XPATH,'//a[contains(@href,"/VehicleHistory/")]')
        vin_history_url = elem_vin.get_attribute("href")
        
        self.vehicles.append(vehicle.Vehicle(url, year, company, model, vin_history_url, image, miles, price, transmission_type))

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
    