from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://tees.co.id")

try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
    print("Pop Up muncul")
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]').click()
    print("Pup Up diclose")

except TimeoutException:
    print("Pop Up tidak muncul")
    pass

time.sleep(3)

driver.close()