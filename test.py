from selenium import webdriver
from selenium.webdriver.common.by import By
import vehicle
import re
import time
import automator
from selenium.webdriver.common.proxy import Proxy, ProxyType
import undetected_chromedriver as uc
from selenium_stealth import stealth


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--window-size=1920x1080")

url = "https://www.carvana.com/vehicle/2644429"

browser = webdriver.Chrome(options=options)

stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

image = ''
fuel = 'Diesel'

newVehicle = vehicle.Vehicle(url, image, fuel)

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
newVehicle.model_year_company_miles_price_setter(model, year, company, miles, price)

# Basic information
browser.execute_script("window.scrollTo(0, 2194)") 
elems_li = browser.find_elements(By.CLASS_NAME, 'sc-4436f562-5')
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
elem_vin = browser.find_element(By.XPATH,'//a[contains(@href,"/VehicleHistory/")]')
vin_history_url = elem_vin.get_attribute("href")
newVehicle.transmission_color_vinHistoryURL_setter(transmission_type, color, vin_history_url)

print("vehicle url: " + newVehicle.url)
print("year: " + str(newVehicle.year))
print("company: "+ newVehicle.company)
print("model: "+ newVehicle.model)
print("vin history url: " + newVehicle.vin_history_url)
print("image url: " + newVehicle.image)
print("miles : " + str(newVehicle.miles))
print("price : " + str(newVehicle.price))
print("transmission type : " + newVehicle.transmission_type)
print("Exterior color: " + newVehicle.color)
print("fuel type: " + newVehicle.fuel)




browser.quit()
# elem_vin = browser.find_element(By.XPATH,'//a[contains(@data-analytics-id,"Specifications - Previous Use Disclaimer")]')
# elem_vin_location = elem_vin.location
# print(elem_vin_location)
# elem_vin.click()


# elems = browser.find_elements(By.TAG_NAME, 'p')
# elems_p_texts = []
# for elem in elems:
#     elems_p_texts.append(elem.text)

# print(elems_p_texts)
# year_model_text = list(filter(lambda v: re.match('\d\d\d\d.*', v), elems_p_texts))[0]
# print(year_model_text)
# miles_text = list(filter(lambda v: re.match('\d+,\d+ Miles', v), elems_p_texts))[0]
# print(miles_text)
# if (re.match(r'\d+,\d+', '$15,590')):
#     print('ey')
# price_text = list(filter(lambda v: re.match('$\d+,\d+', v), elems_p_texts))
# print(price_text)
# txt = elems[2].text.split(' ')[0].replace(',', '')
# price = int(elems[4].text.strip('$').replace(',', ''))
# print(txt)
# print(elems[8].text.split(',')[0])


# # gets all the attributes
# attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', a)
# print(attrs)


# browser.execute_script("window.scrollTo(0, 2194)") 
# elems_li = browser.find_elements(By.CLASS_NAME, 'sc-4436f562-5')
# elems_li_texts = []
# for elem in elems_li:
#     elems_li_texts.append(elem.text)
# print(elems_li_texts)

# if list(filter(lambda v: re.match(r'^Auto.*', v), elems_li_texts)) == []:
#     if list(filter(lambda v: re.match(r'^Manual.*', v), elems_li_texts)) == []:
#         if list(filter(lambda v: re.match(r'^CVT.*', v), elems_li_texts)) == []:
#             transmission_type = None
#         else:
#             transmission_type = 'CVT'
#     else:
#         transmission_type = 'Manual'
# else:
#     transmission_type = 'Automatic'
# print(transmission_type)

