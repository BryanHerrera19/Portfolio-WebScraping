from automator import Automator
import vehicle
from mongoDB import *
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# api key = OXSGUTEI6GOUXRLQZVFT2Z7HWXMDFWBW

class Scraper(Automator):
    website_urls = []
    vehicles = []
    
    def feed_urls_imgs(self):
        self.automate_website()
        # reduced number of car urls
        self.website_urls = self.urls
        images = self.images
        fuels = self.fuels
        for i, url in enumerate(self.website_urls):
            self.scrape_no_vin_info(url, images[i], fuels[i])


    def scrape_no_vin_info(self, url, image, fuel):
        newVehicle = vehicle.Vehicle(url, image, fuel)

        self.browser.get(url)
        self.browser.execute_script("window.scrollTo(0, 500)") 
        time.sleep(2)
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
        time.sleep(3)
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
        color_texts = list(filter(lambda v: re.match(r'.* Exterior Color', v), elems_li_texts))
        if color_texts != []:
            color_text = color_texts[0]
            color = color_text.split()[0]
        else:
            color = ''
        vin = ''
        try:
            vin_text = list(filter(lambda v: re.match(r'VIN: .*', v), elems_li_texts))[0]
            vin = re.findall(r'VIN: (.*)', vin_text)[0]
        except IndexError:
            pass
        self.browser.execute_script("window.scrollTo(0, 2720)") 
        time.sleep(2)
        elem_vin = self.browser.find_element(By.XPATH,'//a[contains(@data-analytics-id, "Specifications - Previous Use Disclaimer")]')
        vin_history_url = elem_vin.get_attribute("href")
        newVehicle.transmission_color_vinHistoryURL_vin_setter(transmission_type, color, vin_history_url, vin)

        # click the link to history
        elem_vin.click()
        self.scrape_vin_info(newVehicle)

    def scrape_vin_info(self, newVehicle):
        # manually click captcha
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(20)
        elems_div = self.browser.find_elements(By.CLASS_NAME,'history-overview-cell')
        elems_div_texts = [x.text for x in elems_div]


        try:
            text = list(filter(lambda v: re.match(r'.* Previous owners', v), elems_div_texts))[0]
            num_text = re.findall('\d+', text)[0]
            num_owners = int(num_text)
        except IndexError:
            try: 
                text = list(filter(lambda v: re.match(r'CARFAX 1-Owner vehicle', v), elems_div_texts))[0]
                num_owners = 1
            except IndexError:
                num_owners = 0

        accidents_text = list(filter(lambda v: re.match(r'.*accident.*', v), elems_div_texts))[0]
        if re.findall('No', accidents_text)[0]:
            accidents = False
        else: 
            accidents = True

        try:
            last_state_text = list(filter(lambda v: re.match(r'Last owned in.*', v), elems_div_texts))[0]
            last_state = re.findall(r'Last owned in (.*)', last_state_text)[0]
        except IndexError:
            last_state = ''
            
        try:
            if list(filter(lambda v: re.match(r'Regular oil changes', v), elems_div_texts))[0]:
                regular_oil_changes = True
        except IndexError:
            regular_oil_changes = False


        try:
            usage_text = list(filter(lambda v: re.match(r'Types of owners: .*', v), elems_div_texts))[0]
            usage = re.findall(r'Types of owners: (.*)', usage_text)[0]
        except IndexError:
            usage = 'Personal'

        newVehicle.vin_history_setter(num_owners, accidents, last_state, regular_oil_changes, usage)

        self.vehicles.append(newVehicle)
        print("appended")
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

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
    print("number of owners : " + str(vehicle.num_owners))
    print("accidents : " + str(vehicle.accidents))
    print("last_state: " + vehicle.last_state)
    print("regular oil changes: " + str(vehicle.regular_oil_changes))
    print("usage: " + vehicle.usage)
    print("vin: " + vehicle.vin)

    if(not alreadyExists(vehicle.url)):
        newCarDict = createCarInfoDict(vehicle, createVINHistInfoDict(vehicle))
        insertCarInfo(newCarDict)
    else:
        updatedDict = createCarInfoDict(vehicle, createVINHistInfoDict(vehicle))
        updateDB(vehicle.url, updatedDict)