import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_actions():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")

    # Find the iframe element
    iframe = driver.find_element(By.TAG_NAME, "iframe")

    # Scroll the iframe into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", iframe)

    # Perform the action chain after the iframe is in view
    ActionChains(driver).scroll_to_element(iframe).perform()

    # Wait for 10 seconds
    time.sleep(10)

    driver.quit()


if __name__ == "__main__":
    test_actions()


