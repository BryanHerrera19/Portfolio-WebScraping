from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import automator

url = "https://www.carvana.com/vehicle/2491477"
browser = webdriver.Chrome()
browser.maximize_window() # For maximizing window

browser.get(url)

browser.execute_script("window.scrollTo(0, 500)") 
time.sleep(3)
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

# elems = browser.find_elements(By.TAG_NAME, 'p')
# for elem in elems:
#     print(elem.text)
# print(elems[2].text)
# a = browser.execute_script("return arguments[0].parentNode;", elems[2])
# elem = ''
# # gets all the attributes
# attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', a)
# print(attrs)

# elem = int(browser.find_element(By.CLASS_NAME, 'gap-x-8').text.strip('$').replace(',',''))
# attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', elem)
# print(elem)
# print(attrs)
# print(elem.text)
# miles_parts = int(re.findall(r'\d+,\d+', elem.text)[0].replace(',', ''))
# # miles = int(''.join([str(x) for x in miles_parts]))
# print(miles_parts)
# # miles = browser.find_element(By.CLASS_NAME, 'sc-5e8cfdb6-6').text.split(' ')[0].replace(',', '')
# # print(miles)
# price = browser.find_element(By.XPATH,'//p[contains(@data-qa,"hero-header-price")]').text
# print(price)

browser.execute_script("window.scrollTo(0, 2194)") 
elems_li = browser.find_elements(By.CLASS_NAME, 'sc-4436f562-5')
elems_li_texts = []
for elem in elems_li:
    elems_li_texts.append(elem.text)
print(elems_li_texts)

if list(filter(lambda v: re.match(r'^Auto.*', v), elems_li_texts)) == []:
    if list(filter(lambda v: re.match(r'^Manual.*', v), elems_li_texts)) == []:
        if list(filter(lambda v: re.match(r'^CVT.*', v), elems_li_texts)) == []:
            transmission_type = None
        else:
            transmission_type = 'CVT'
    else:
        transmission_type = 'Manual'
else:
    transmission_type = 'Automatic'
print(transmission_type)
# if(re.match(r'.*Electric.*',elems_li[0].text)):
#     transmission_type = elems_li[6].text.split(',')[0]
# else:
#     transmission_type = elems_li[5].text.split(',')[0]
# if (re.match(r'Auto.*',transmission_type)):
#     transmission_type = 'Automatic'
# print(transmission_type)
# transmission_type = elems_li[8]
# elems = browser.find_elements(By.CLASS_NAME, 'sc-4436f562-5')
# for elem in elems:
#     print(elem.text)
# print(elems[5].text.split(',')[0])

# Automator = automator.Automator
# Automator.get_vehicle_urls_imgs(Automator)
# website_urls = Automator.urls
# for i, url in enumerate(website_urls):
#     print(url)
#     browser = webdriver.Chrome()
#     browser.maximize_window() # For maximizing window
#     browser.implicitly_wait(30) # gives an implicit wait for 20 seconds
#     browser.get(url)
#     browser.execute_script("window.scrollTo(0, 1000)") 
#     elem = browser.find_element(By.CLASS_NAME, 'sc-5e8cfdb6-6')
#     print(elem.text)
#     miles_parts = int(re.findall(r'\d+,\d+', elem.text)[0].replace(',', ''))
#     print(miles_parts)

        # browser.execute_script("window.scrollTo(0, 6177)") 
        # elem_inspection = browser.find_element(By.ID,'inspection-150-point')
        # elems_inspection_p = elem_inspection.find_elements(By.TAG_NAME, 'p')
        # texts = elems_inspection_p[1].text.split()
        # year = int(texts[1])
        # company = texts[2]
        # model = texts[3]