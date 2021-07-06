import time
import threading

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click(element):
    while True:
        element.click()


driver = webdriver.Firefox()
driver.get("https://clickspeedtest.com/")

WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#ez-accept-all')))

driver.find_element_by_css_selector('#ez-accept-all').click()

element = driver.find_element_by_css_selector('#clicker')

t = threading.Thread(target=click, args=[element])
t.start()
t2 = threading.Thread(target=click, args=[element])
t2.start()
t2.join()
