from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rabbit.t3n4ci0us-noah.repl.co/")
while True:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/h1"))
        )
    result = element.text.replace("Go ", "")
    print(result)
    driver.get(f"https://rabbit.t3n4ci0us-noah.repl.co/{result}")
#driver.close()