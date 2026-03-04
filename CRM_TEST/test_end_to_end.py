from driver_setup import setup_driver
from login import login
from CRM_form import crm_form, crm_displayed, crm_leads, all_leads, lead_details_page
from selenium.webdriver.common.by import By
import time

def complete_test():
    driver = setup_driver()

    try:
        login(driver)

        crm_displayed(driver)

        crm_form(driver)

        crm_leads(driver)

        all_leads(driver)

        lead_details_page(driver)

        time.sleep(10)

    except Exception as e:
        print("Test failed:", str(e))

    finally:
        driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    complete_test()





