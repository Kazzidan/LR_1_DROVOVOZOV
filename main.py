from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service("G:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://adminqa.neapro.site/login')
driver.set_window_size(1024, 600)
driver.minimize_window()
driver.find_element(By.CSS_SELECTOR, '.email input').click()
driver.find_element(By.CSS_SELECTOR, '.email input').send_keys('blackleprosy@gmail.com')
driver.find_element(By.CSS_SELECTOR, '.password input').click()
driver.find_element(By.CSS_SELECTOR, '.password input').send_keys('123456789')
# верстка была изменена, невохможно взять селектор кнопка, она теперь не button, а input
# у нее нет класса или id
driver.find_element(By.CSS_SELECTOR, '.input').click()

