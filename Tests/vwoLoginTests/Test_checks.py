import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By


def test_checks():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    ch_bx = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    for c in ch_bx:
        if not c.is_selected():
            c.click()
    time.sleep(10)
