import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.find_element(By.ID, "click").click()
    actions = ActionBuilder(driver)
    actions.pointer_action.pointer_down(MouseButton.BACK)
    actions.pointer_action.pointer_down(MouseButton.BACK)
    actions.perform()
    print("Are done here")
    time.sleep(10)