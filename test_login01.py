from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def test_driver():
    browser = webdriver.Chrome()
    yield browser
    return browser


def test_testid(test_driver):
    test_driver.get("https://app.vwo.com/")
    print(test_driver.title)
    assert "Login - VWO" == test_driver.title, "you've written an wrong code"
