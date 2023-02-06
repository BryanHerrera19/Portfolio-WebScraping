from selenium import webdriver
from selenium.webdriver.common.by import By

class Automator:
    website_url = "https://www.carvana.com/cars"
    browser = webdriver.Chrome()
    urls = []

    def get_vehicle_urls(self):
        self.browser.get(self.website_url)
        elems = self.browser.find_elements(By.XPATH,'//a[contains(@href,"/vehicle/")]')
        
        for elem in elems:
            self.urls.append(elem.get_attribute("href"))
        print(self.urls)

Automator = Automator()

Automator.get_vehicle_urls()