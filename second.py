import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

while True:
    start = time.time()
    # get the cookie and click it
    try:
        cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
        cookie.click()
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
