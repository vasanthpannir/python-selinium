import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_acions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    click = driver.find_element(By.ID,"clickable")
    actions = ActionChains(driver)
    actions.click_and_hold(click).key_down(Keys.SHIFT).send_keys("pramod").key_up(Keys.SHIFT).perform()
    time.sleep(20)