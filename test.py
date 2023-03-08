import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller
import subprocess
import vehicle
import re
import shutil

from mongoDB import *
import vehicle
import re
import time
import automator

# using debugger and cookie (by not deleting them), trick the system to get undetected as a bot
# however, after few times, gets blocked
# attempted to delete the cookie and use extension to solve captcha but debugger mode does not support chrom extension

try:
    shutil.rmtree(r"C:\chrometemp")  # remove Cookie, Cache files
except FileNotFoundError:
    pass

try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')   # Open the debugger chrome
    
except FileNotFoundError:
    subprocess.Popen(r'C:\Users\binsu\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')

option = Options()


option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
option.add_extension(r'C:\Users\gkim5\OneDrive\문서\2023 Spring\COMP 195\senior-project-spring-2023-web-scraping\extension.crx')


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    browser = webdriver.Chrome(options=option)
    
except:
    chromedriver_autoinstaller.install(True)
    browser = webdriver.Chrome(options=option)
browser.implicitly_wait(10)

url = 'https://www.carvana.com/vehicle/2452937'
image = ''
fuel = 'Gas'

browser.maximize_window()
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

time.sleep(10)
browser.find_element(By.XPATH,'//a[contains(@data-analytics-id, "Specifications - Previous Use Disclaimer")]').click()
# click vin history link
time.sleep(10)
browser.switch_to.window(browser.window_handles[1])
elems_div = browser.find_elements(By.CLASS_NAME,'history-overview-cell')
elems_div_texts = []
for elem in elems_div:
       elems_div_texts.append(elem.text)


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

if(alreadyExists(newVehicle.url) == False):
        newCarDict = createCarInfoDict(newVehicle)
        insertCarInfo(newCarDict)
browser.close()