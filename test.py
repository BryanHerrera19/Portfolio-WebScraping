from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.carvana.com/vehicle/2631387"
browser = webdriver.Chrome()
browser.maximize_window() # For maximizing window
browser.implicitly_wait(30) # gives an implicit wait for 20 seconds
browser.get(url)
browser.execute_script("window.scrollTo(0, 112)") 
elems = browser.find_elements(By.CLASS_NAME, 'Layered-spinner64__sc-vss3bj-0')
elem = elems[3].find_element(By.TAG_NAME, 'div')
elem1 = elem.find_element(By.XPATH,'//img[@role="presentation"]')
print(elem1.get_attribute("src"))

