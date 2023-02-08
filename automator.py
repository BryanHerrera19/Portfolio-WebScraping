from selenium import webdriver
from selenium.webdriver.common.by import By

class Automator:
    website_url = "https://www.carvana.com/cars"
    images = []
    urls = []

    def get_vehicle_urls_imgs(self):
        browser = webdriver.Chrome()
        browser.get(self.website_url)
        elems = browser.find_elements(By.XPATH,'//a[contains(@href,"/vehicle/")]')
        
        for elem in elems:
            url = elem.get_attribute("href")
            self.urls.append(url)
            img_elem = elem.find_element(By.TAG_NAME,'img')
            img_url = img_elem.get_attribute("src")
            self.images.append(img_url)
            print(url + " " + img_url)


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
# Automator.get_vehicle_urls_imgs()
# print(Automator.get_vin_history_url("https://www.carvana.com/vehicle/2631387"))
