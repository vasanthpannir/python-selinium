import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()  # Correctly instantiate the WebDriver
    yield driver
    driver.quit()  # Ensure driver.quit() is called properly


@pytest.mark.usefixtures("driver")
def test_js01(driver):
    url = "https://the-internet.herokuapp.com/add_remove_elements/"
    driver.get(url)

    # Wait for the "Add Element" button to be clickable and click it
    wait = WebDriverWait(driver, 10)
    add_element_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='addElement()']")))
    driver.execute_script("arguments[0].click();", add_element_button)

    # Wait to observe the change
    time.sleep(2)

    # Verify the element is added
    added_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.added-manually")))
    assert added_element.is_displayed(), "Element was not added."

    # Get the page title using JavaScript
    title = driver.execute_script("return document.title")
    print(f"Page title is: {title}")

    # Scroll the window using JavaScript
    driver.execute_script("window.scrollBy(0, 100);")

    # Clean up: Remove the element by clicking the delete button
    driver.execute_script("arguments[0].click();", added_element)

    # Wait to observe the change
    time.sleep(2)

    # Verify the element is removed
    assert len(driver.find_elements(By.CSS_SELECTOR, "button.added-manually")) == 0, "Element was not removed."


if __name__ == "__main__":
    pytest.main()