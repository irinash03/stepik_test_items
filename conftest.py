import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    language = request.config.getoption("language")
    if language == "es":
        browser.get("http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/")
        time.sleep(20)
    elif language == "fr":
        browser.get("http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/")
        time.sleep(20)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()



