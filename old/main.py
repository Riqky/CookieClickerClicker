import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")

while True:
    start = time.time()
    # get the cookie and click it
    try:
        driver.find_element(By.CSS_SELECTOR, '#bigCookie').click()
    except:
        pass

    #find the upgrades
    upgrades = driver.find_elements_by_css_selector("div.product.enabled")

    for item in upgrades:
        item.click()

    upgrades = driver.find_elements_by_css_selector("div.upgrade.enabled")

    for item in upgrades:
        item.click()

    print(round(time.time() - start, 2))
