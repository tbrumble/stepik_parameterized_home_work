import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language for browser startup")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_language = request.config.getoption("language")
    print("\nselected language: " + browser_language)
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
