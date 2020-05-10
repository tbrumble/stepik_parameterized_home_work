import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasket:
    @pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_purchases_button_is_exists_and_work(self, browser, link):
        print("\nstart test_button_is_exists..")
        try:
            print("\nopen link: " + link)
            browser.get(link)
            print("\nsleep")
            time.sleep(30)
            print("\nget button")
            button = browser.find_element_by_css_selector("#add_to_basket_form > button")
            assert button is not None, "No add to cart button"
            print("\nbutton click")
            button.click()
            print("\nwait messages")
            WebDriverWait(browser, 7).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#messages"))
            )
            print("\nget message element 1")
            div_element1 = browser.find_element_by_css_selector("#messages > div:nth-child(1)")
            assert div_element1 is not None, "Add to cart button doesn't show message 1"
            print("\nget message element 2")
            div_element2 = browser.find_element_by_css_selector("#messages > div:nth-child(2)")
            assert div_element2 is not None, "Add to cart button doesn't show message 2"
            print("\nget message element 3")
            div_element3 = browser.find_element_by_css_selector("#messages > div:nth-child(3)")
            assert div_element3 is not None, "Add to cart button doesn't show message 3"
        finally:
            print("\nend test_button_is_exists..")
            time.sleep(10)
