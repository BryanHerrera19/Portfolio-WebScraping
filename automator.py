from selenium import webdriver
from selenium.webdriver.common.by import By

class Automator:
    website_url = "https://www.carvana.com/cars"
    urls = []

    def get_vehicle_urls(self):
        browser = webdriver.Chrome()
        browser.get(self.website_url)
        elems = browser.find_elements(By.XPATH,'//a[contains(@href,"/vehicle/")]')
        
        for elem in elems:
            self.urls.append(elem.get_attribute("href"))
        print(self.urls)

    # probably won't use this method because it makes more sense to do it in Scraper class scrape_no_vin_info()
    # def get_vin_history_url(self, url):
    #     browser = webdriver.Chrome()
    #     browser.implicitly_wait(10)
    #     browser.get(url)
    #     browser.execute_script("window.scrollTo(0, 2194)") 
    #     elem = browser.find_element(By.XPATH,'//a[contains(@href,"/VehicleHistory/")]')
    #     # print(elem.location)
    #     return elem.get_attribute("href")

# Automator = Automator()
# print(Automator.get_vin_history_url("https://www.carvana.com/vehicle/2631387"))
