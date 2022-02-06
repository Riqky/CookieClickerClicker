import _thread
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from clicker import click

driver = webdriver.Firefox()
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#bigCookie')))

# cookie_position = cookie.location

location = driver.get_window_position()
cookiePos = (cookie.location["x"] + location["x"],
             cookie.location["y"] + location["y"])

print(cookiePos)

# get the cookie and click it
# this time on a different thread!
_thread.start_new_thread(click, (0, cookiePos))

try:
    while True:

        # find the upgrades
        upgrades = driver.find_elements_by_css_selector("div.product.enabled")

        for item in upgrades:
            item.click()

        upgrades = driver.find_elements_by_css_selector("div.upgrade.enabled")

        for item in upgrades:
            item.click()
except KeyboardInterrupt:
    driver.close()
    driver.quit()
