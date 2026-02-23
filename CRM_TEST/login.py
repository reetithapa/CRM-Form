from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def login(driver):
    driver.get("https://app-ispaas.dev.geniussystems.com.np")

    wait = WebDriverWait(driver, 10)
    #assert "login" in driver.current_url, "User is not directed to login page"

    login_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Sign in to your account']")))
    print("Sign in to your account visible")
    #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg"))).click()
    company_code = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter code']")))
    company_code.send_keys("ctn")

    username = driver.find_element(By.ID, ":r1:")
    username.send_keys("reeti")

    password = driver.find_element(By.ID, ":r2:")
    password.send_keys("Reeti@123")

    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

    print("Login Successful")



