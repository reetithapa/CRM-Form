from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def crm_form(driver):
    wait = WebDriverWait(driver, 10)

    New_Lead = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button']")))
    New_Lead.click()
    assert "/crm/lead/add" in driver.current_url
    time.sleep(1)

    primary_mobile = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Primary Mobile']")))
    primary_mobile.send_keys("9861595668")
    time.sleep(1)

    service_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='service_type']"))
    service_type.select_by_visible_text("FTTH")
    time.sleep(1)

    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name.send_keys("Abc1")
    time.sleep(1)

    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("Xyz@123")
    time.sleep(1)

    email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    email.send_keys("ab_12@gmail.com")
    time.sleep(1)

    preferred_username = driver.find_element(By.XPATH, "//input[@placeholder='Preferred Username']")
    preferred_username.send_keys("ABC")
    time.sleep(1)

    interested_product_group = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m")))
    interested_product_group.click()
    interested_product_option = driver.find_element(By.XPATH, "//div[text()='business-50 mbs']")
    interested_product_option.click()
    #interested_product_group = driver.find_element(By.XPATH, "//div[text()='50 mbps packages']")
    #interested_product_group.select_by_visible_text("50 mbps packages")
    time.sleep(1)

    interested_product_option = driver.find_element(By.ID, "react-select-5-input")
    interested_product_option.click()
    interested_product = driver.find_element(By.XPATH, "//div[text()='Business - 50 mbps (Price:4444.711/Renew:3371.26)']")
    interested_product.click()
    time.sleep(1)

    entry_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='entry_source']"))
    entry_source.select_by_visible_text("Social Media")
    time.sleep(1)

    lead_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_source']"))
    lead_source.select_by_visible_text("Advertisements")
    time.sleep(1)

    assigned = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
    assigned.click()
    assigned_option = driver.find_element(By.XPATH, "//div[text()=' (ias@geniussystems.com.np) ']")
    assigned_option.click()
    time.sleep(1)

    lead_status = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_status']"))
    lead_status.select_by_visible_text("Warm")
    time.sleep(1)

    existing_isp = Select(driver.find_element(By.XPATH, "//select[@data-testid='existing_isp']"))
    existing_isp.select_by_visible_text("Worldlink")
    time.sleep(1)

    profession = driver.find_element(By.XPATH, "//input[@placeholder='Enter profession']")
    profession.send_keys("Teacher")
    time.sleep(1)

    address = driver.find_element(By.XPATH, "//input[@placeholder='Address']")
    address.send_keys("Baneshwor")
    time.sleep(1)

    proceed = driver.find_element(By.XPATH, "//button[text()='Proceed']")
    proceed.click()
    time.sleep(2)















