import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By

def test_tables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    row = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row_len = len(row)
    print(row_len)

    col = driver.find_elements(By.XPATH,value="//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col_len = len(col)
    print(col_len)

    fp = "//table[contains(@id,'cust')]/tbody/tr["
    sp = "]/td["
    lp ="]"

    for i in range(2,row_len+1):
        for j in range(1,col_len+1):
            dynamic_path = f"{fp}{i}{sp}{j}{lp}"
            data = driver.find_element(By.XPATH, dynamic_path).text
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")

        #     print(data.text,end=" ")
        # print()
        #     # data = driver.find_element(By.XPATH,dynamic_path)
        #     # print(data)


    driver.quit()

# def test_tables():
#     driver = webdriver.Chrome()
#     driver.get("https://awesomeqa.com/webtable.html")
#
#     # Find all rows in the table
#     rows = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
#     row_len = len(rows)
#     print(row_len)
#
#     # Find all columns in the second row
#     cols = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
#     col_len = len(cols)
#     print(col_len)
#
#     fp = "//table[contains(@id,'cust')]/tbody/tr["
#     sp = "]/td["
#     lp = "]"
#
#     for i in range(2, row_len + 1):
#         for j in range(1, col_len + 1):
#             dynamic_path = f"{fp}{i}{sp}{j}{lp}"
#             data = driver.find_element(By.XPATH, dynamic_path)
#             print(data.text, end=" ")
#         print()  # To print each row in a new line
#
#     driver.quit()

