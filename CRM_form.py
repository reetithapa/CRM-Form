import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def crm_form(driver):
    New_Lead = driver.find_element(By.XPATH, "//button[type='button']")
    New_Lead.click()
    assert "/crm/lead/add" in driver.current_url

    with open ("testdata/lead.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:

         primary_mobile = driver.find_element(By.ID, ":r9:")
         primary_mobile.send_keys(row["Primary_mobile"])

         service_type = Select(driver.find_element(By.ID, ":r1o:"))
         service_type.select_by_visible_text(row["Service_type"])

         first_name = driver.find_element(By.ID, ":r17:")
         first_name.send_keys(row["First_name"])

         last_name = driver.find_element(By.ID, ":r18:")
         last_name.send_keys(row["Last_name"])

         email = driver.find_element(By.ID, ":r2h:")
         email.send_keys(row["Email"])

         preferred_username = driver.find_element(By.ID, ":r2i:")
         preferred_username.send_keys(row["Preferred_username"])

         interested_product_group = Select(driver.find_element(By.ID, "service_id"))
         interested_product_group.select_by_visible_text(row["Interested_product_group"])

         entry_source = Select(driver.find_element(By.ID, ":r2m:"))
         entry_source.select_by_visible_text(row["Entry_source"])

         lead_source = Select(driver.find_element(By.ID, ":r2n:"))
         lead_source.select_by_visible_text(row["Lead_source"])

         assigned = Select(driver.find_element(By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m"))
         assigned.select_by_visible_text(row["Assign_to_me"])

         lead_status = Select(driver.find_element(By.ID, ":r2p:"))
         lead_status.select_by_visible_text(row["Lead_status"])

         existing_isp = Select(driver.find_element(By.ID, ":r2q:"))
         existing_isp.select_by_visible_text(row["Existing_ISP"])

         address = driver.find_element(By.ID, ":r1i:")
         address.send_keys(row["Address"])

         proceed = driver.find_element(By.XPATH, "//button[text()='Proceed']")
         proceed.click()











