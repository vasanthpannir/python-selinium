import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_acions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.NAME,"firstname")
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"the testing academy").key_up(Keys.SHIFT).perform()
    url = driver.find_element(By.XPATH,"//a[normalize-space()='Click here to Download File']")
    actions.context_click(url).perform()
    time.sleep(20)