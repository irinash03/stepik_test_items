from selenium.common.exceptions import NoSuchElementException

def check_exists_by_xpath(xpath, browser):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def test_bin_button_exist(browser):
    assert (check_exists_by_xpath(".//div[@class='col-sm-6 product_main']//form[1]/button", browser)) == True



