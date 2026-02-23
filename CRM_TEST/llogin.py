from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    return driver


def login(driver):
    driver.get("https://app-ispaas.dev.geniussystems.com.np")

    wait = WebDriverWait(driver, 10)
    #assert "login" in driver.current_url, "User is not directed to login page"

    login_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Sign in to your account']")))
    print("Sign in to your account visible")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.flex.ml-2.gap-1.border.bg-slate-50.p-1.rounded-lg.items-center.hover:bg-slate-200.cursor-pointer"))).click()

    company_code = driver.find_element(By.XPATH, "//div[@data-testid='input-div']")
    company_code.send_keys("ctn")

    username = driver.find_element(By.ID, ":r1:")
    username.send_keys("reeti")

    password = driver.find_element(By.ID, ":r2:")
    password.send_keys("Reeti@123")

    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    login_button.click()

def crm():
    driver = setup_driver()

    try:
        login(driver)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    crm()
