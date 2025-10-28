import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

driver = None

def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome")


@pytest.fixture(scope="class")
def setUpDriver(request):
    global driver
    #Para hacer que podamos elegir en qué navegador correr nuestros TC desde la consola CMD, utilizaremos la siguiente sintaxis
    browserName = request.config.getoption("browserName")
    if browserName.lower() == "chrome":
        service_obj = ChromeService("C:\\Users\\mari_\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=ChromeOptions())
    elif browserName.lower() == "firefox":
        options = FirefoxOptions()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

        service_obj = FirefoxService(r"C:\Users\mari_\Downloads\geckodriver-v0.36.0-win-aarch64\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj, options=FirefoxOptions())
    else:
        print("Unknown browser")

    driver.get("https://www.mercadolibre.com/")
    driver.implicitly_wait(2)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver
    driver.quit()