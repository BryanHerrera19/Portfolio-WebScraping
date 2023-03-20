import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import vehicle
import re

# using chrome extension, solve captcha
# there is a quota for api, so created personal api key
# have to input the api key first

option = Options()

option.add_extension(r'C:\Users\gkim5\OneDrive\문서\2023 Spring\COMP 195\senior-project-spring-2023-web-scraping\extension.crx')

browser = webdriver.Chrome(options=option)
    
url = 'chrome-extension://mpbjkejclgfgadiemmefgebjfooflfhl/src/options/index.html'

# api key = OXSGUTEI6GOUXRLQZVFT2Z7HWXMDFWBW
browser.maximize_window()
browser.get(url)
time.sleep(30)

url = 'https://www.carvana.com/vehicle/2651229'
image = ''
fuel = 'Gas'


browser.get(url)
newVehicle = vehicle.Vehicle(url, image, fuel)

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

browser.execute_script("window.scrollTo(0, 2900)") 
time.sleep(2)
# click the link to history
browser.find_element(By.XPATH,'//a[contains(@data-analytics-id, "Specifications - Previous Use Disclaimer")]').click()

# manually click captcha
time.sleep(30)
browser.switch_to.window(browser.window_handles[1])
elems_div = browser.find_elements(By.CLASS_NAME,'history-overview-cell')
elems_div_texts = [x.text for x in elems_div]


try:
    text = list(filter(lambda v: re.match(r'.* Previous owners', v), elems_div_texts))[0]
    num_text = re.findall('\d+', text)[0]
    num_owners = int(num_text)
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
    usage = list(filter(lambda v: re.match(r'.*vehicle', v), elems_div_texts))[0]
except IndexError:
    usage = ''

newVehicle.vin_history_setter(num_owners, accidents, last_state, regular_oil_changes, usage)

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
print("number of owners : " + str(newVehicle.num_owners))
print("accidents : " + str(newVehicle.accidents))
print("last_state: " + newVehicle.last_state)
print("regular oil changes: " + str(newVehicle.regular_oil_changes))
print("usage: " + newVehicle.usage)

browser.close()
