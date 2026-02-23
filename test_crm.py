from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def crm_displayed(driver):
    wait = WebDriverWait(driver, 10)

    CRM = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='CRM']")))
    CRM.click()

    assert "https://app-ispaas.dev.geniussystems.com.np/crm/" in driver.current_url

