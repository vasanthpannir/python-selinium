# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
#
#
#
# def test_actions():
#     driver = webdriver.Firefox()
#     driver.get("https://www.makemytrip.com/")
#     mv_01 = driver.find_element(By.XPATH,"//label[@for='fromCity']")
#     ActionChains(driver).move_to_element(mv_01).send_keys("Bengaluru").perform()
#     time.sleep(10)


import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_actions():
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.makemytrip.com/")

        # Wait for the "From" city label to be present and clickable
        wait = WebDriverWait(driver, 10)
        mv_01 = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='fromCity']")))

        # Move to the element and click on it to make the input field active
        ActionChains(driver).move_to_element(mv_01).click().perform()

        # Wait for the input field to be present
        input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='From']")))

        # Click on the input field to focus and send keys to the input field
        input_field.click()
        input_field.send_keys("Bengaluru")

        # Wait for 10 seconds to observe the result
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_actions()
