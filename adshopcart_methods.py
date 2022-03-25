import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'----- SET UP FUNCTION --------------------------------------------')
    print(f'The test started at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.hmpg_url)
    if driver.current_url == locators.hmpg_url and locators.hmpg_title in driver.title:
        print(f'{locators.app} launched successfully.')
        print(f'{locators.app} homepage url:{driver.current_url}, title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. Check your code or app.')
        print(f'current url: {driver.current_url}, page title: {driver.title}')



def tearDown():
    if driver is not None:
        print('----- TEAR DOWN FUNCTION ----------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# setUp()
# tearDown()
