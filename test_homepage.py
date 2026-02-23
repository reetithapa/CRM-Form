from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def homepage(driver):
    wait = WebDriverWait(driver, 10)

    Home = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-testid='Home']")))




