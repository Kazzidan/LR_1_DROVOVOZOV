from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

s = Service("G:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get('https://qa.neapro.site/login')
driver.set_window_size(1024, 600)
driver.minimize_window()
driver.find_element(By.XPATH, "//div[@class='field']/input[@type='text']").click()
driver.find_element(By.XPATH, "//div[@class='field']/input[@type='text']").send_keys('blackleprosy@gmail.com')
driver.find_element(By.XPATH, "//div[@class='field']/input[@type='password']").click()
driver.find_element(By.XPATH, "//div[@class='field']/input[@type='password']").send_keys('123456789')
driver.find_element(By.XPATH, "//button[@class='btn fill']").click()

