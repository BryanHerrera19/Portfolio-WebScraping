from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium.webdriver.support.relative_locator import locate_with

class Automator:
    website_url = "https://www.carvana.com/cars"
    images = []
    fuels = []
    urls = []
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--window-size=1920x1080")

    options.binary_location="C:\Program Files\Google\Chrome\Application\chrome.exe"
    browser = webdriver.Chrome(options=options)
    # setup value to act like human
    browser.execute_script("Object.defineProperty(navigator, 'language',{get: function() {return ['en-US','en']}})")
    browser.execute_script("Object.defineProperty(navigator, 'plugins',{get: function() {return[1,2,3,4,5]}})")


    def automate_website(self):
        # browser = webdriver.Chrome(options=self.options)
        # browser = webdriver.Chrome()
        self.browser.maximize_window() # For maximizing window
        self.browser.implicitly_wait(10)
        self.browser.get(self.website_url)

        fuel_types = ['Gas', 'Electric', 'Hybrid', 'Diesel']
        # <div role="button" tabindex="0" class="border-0 border-t border-grey-2 border-solid items-center flex py-24 px-32 relative text-left transition-shadow w-full justify-between" data-qa="list-item-header" data-analytics-id="filters.expandfacet-fuelTypes-headerButton" data-test="ListItemHeader"><p class="text-blue-6 t-header-s uppercase mb-0">Fuel</p><svg class="h-24 w-24 text-blue-2" viewBox="-5 -8 20 20"><g id="arrow-down-10x6-blue" class="ae-mutation-ignore"><path d="M0,.81a.78.78,0,0,0,.23.55L4.52,5.74A.9.9,0,0,0,5.16,6a.88.88,0,0,0,.63-.28l4-4.38A.77.77,0,0,0,9.71.2a.88.88,0,0,0-1.2.08L5.13,4,1.48.26A.88.88,0,0,0,.27.22.78.78,0,0,0,0,.81" fill="#00aed9"></path></g></svg></div>
        for fuel in fuel_types:
            buttons = self.browser.find_elements(By.CLASS_NAME, 'DropDownMenustyles__DropDownWrap-sc-15ybm7w-0')
            if buttons == []:
                self.style_left_bar(fuel)
                # time.sleep(10000)
            else:
                fuel_filter_button = buttons[5]
                fuel_filter_button.click()
                self.get_fuel_type(fuel)
                # fuel_filter_button.click()
                time.sleep(3)
                self.get_url_imgs(fuel)
                self.browser.get(self.website_url)

    
    def style_left_bar(self, fuel):
        fuels = {'Diesel':0, 'Electric':1, 'Gas':2, 'Hybrid':3}
        fuel_filter_button = self.browser.find_element(By.XPATH, '//div[contains(@data-analytics-id,"filters.expandfacet-fuelTypes-headerButton")]')
        fuel_filter_button.click()
        fuel_filters = self.browser.find_elements(locate_with(By.TAG_NAME, 'label').below(fuel_filter_button))
        fuel_filters[fuels[fuel]].click()
        time.sleep(3)
        self.get_url_imgs(fuel)
        self.browser.get(self.website_url)


    def get_url_imgs(self, fuel):
        elems = self.browser.find_elements(By.XPATH,'//a[contains(@href,"/vehicle/")]')
        for elem in elems:
            url = elem.get_attribute("href")
            self.urls.append(url)
            img_elem = elem.find_element(By.TAG_NAME,'img')
            img_url = img_elem.get_attribute("src")
            self.images.append(img_url)
            self.fuels.append(fuel)
            print(url + " " + img_url+ " " + fuel)

    def get_fuel_type(self, fuel):
        xpath = '//a[contains(@data-cv-test,"filters.fuelTypes.' + fuel + '")]'
        self.browser.find_element(By.XPATH, xpath).click()


# Automator = Automator()
# Automator.automate_website()
