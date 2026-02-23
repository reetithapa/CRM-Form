from driver_setup import setup_driver
from login import login
from test_homepage import homepage
from test_crm import crm_displayed
from CRM_form import crm_form
from selenium.webdriver.common.by import By
import time

def complete_test():
    driver = setup_driver()

    try:
        login(driver)

        homepage(driver)

        crm_displayed(driver)

        crm_form(driver)

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    complete_test()





