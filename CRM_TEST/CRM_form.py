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
    time.sleep(2)

    primary_mobile = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Primary Mobile']")))
    primary_mobile.send_keys("9861595668")
    time.sleep(2)

    service_type = Select(driver.find_element(By.XPATH, "//select[@data-testid='service_type']"))
    service_type.select_by_visible_text("FTTH")
    time.sleep(2)

    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name.send_keys("John")
    time.sleep(2)

    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("Mayor")
    time.sleep(2)

    email = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    email.send_keys("john12@gmail.com")
    time.sleep(2)

    preferred_username = driver.find_element(By.XPATH, "//input[@placeholder='Preferred Username']")
    preferred_username.send_keys("John")
    time.sleep(2)

    interested_product_group = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.react-select__input-container.css-19bb58m")))
    interested_product_group.click()
    interested_product_option = driver.find_element(By.XPATH, "//div[text()='50 mbps packages']")
    interested_product_option.click()
    #interested_product_group = driver.find_element(By.XPATH, "//div[text()='50 mbps packages']")
    #interested_product_group.select_by_visible_text("50 mbps packages")
    time.sleep(2)

    entry_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='entry_source']"))
    entry_source.select_by_visible_text("Social Media")
    time.sleep(2)

    lead_source = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_source']"))
    lead_source.select_by_visible_text("Advertisements")
    time.sleep(2)

    assigned = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.w-[9px].h-[9px].rounded-full.absolute.top-0.5.transition-transform.duration-100.shadow-md.translate-x-0.5.bg-white")))
    assigned.click()
    #assigned_option = driver.find_element(By.XPATH, "//div[text()='(ias@geniussystems.com.np)']")
    #assigned_option.click()
    time.sleep(2)

    lead_status = Select(driver.find_element(By.XPATH, "//select[@data-testid='lead_status']"))
    lead_status.select_by_visible_text("Warm")
    time.sleep(2)

    existing_isp = Select(driver.find_element(By.XPATH, "//select[@data-testid='existing_isp']"))
    existing_isp.select_by_visible_text("Worldlink")
    time.sleep(2)

    address = driver.find_element(By.XPATH, "//input[@placeholder='Address']")
    address.send_keys("Kirtipur")
    time.sleep(2)

    proceed = driver.find_element(By.XPATH, "//button[text()='Proceed']")
    proceed.click()
    time.sleep(2)







