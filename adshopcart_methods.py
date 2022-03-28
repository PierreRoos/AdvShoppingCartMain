import datetime
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

import adshopcart_locators as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # add this import for drop down list

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'----- SET UP FUNCTION --------------------------------------------')
    print(f'The test started at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.hmpg_url)
    if driver.current_url == locators.hmpg_url and locators.hmpg_title in driver.title:
        sleep(2)
        print(f'{locators.app} launched successfully.')
        print(f'{locators.app} homepage url:{driver.current_url}, title: {driver.title}')
    else:
        print(f'{locators.app} did not launch. Check your code or app.')
        print(f'current url: {driver.current_url}, page title: {driver.title}')


def tearDown():
    if driver is not None:
        print('----- TEAR DOWN FUNCTION ------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def register():
    print('----- REGISTER FUNCTION -----------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(.5)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(.5)
    if driver.current_url == locators.register_page_url:
        sleep(0.25)
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(0.25)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phonenum)
        sleep(0.25)
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
        sleep(0.25)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(0.25)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(0.25)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
        sleep(0.25)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(0.25)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.25)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(0.5)
        print(f'registration completed. User is signed in. Username {locators.username} is displayed next to USER icon')
    else:
        print('Registration page did not load. Check your code and website.')


def check_fullname():
    print('----- CHECK FULLNAME FUNCTION -----------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    # driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "My_account"]').click()
    sleep(3)
    if driver.find_element(By.XPATH, f'//label[contains(., "{locators.first_name} {locators.last_name}" )]'):
        print(f'User first and last name displayed: {locators.first_name} {locators.last_name} ')
    else:
        print('Full name is not displayed. Check your code or website.')


def check_orders():
    print('----- CHECK ORDERS FUNCTION -----------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, f'//label[contains(., "- No orders -" )]'):
        print(' This user has no orders. ')
    else:
        print('orders are not displayed. Check your code or website.')


def sign_out():
    print('----- SIGN OUT FUNCTION -----------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(2)
    #driver.find_element(By.XPATH, '//label[contains(., "Sign out")]').click()  # doesnt work
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
    sleep(0.5)
    print(f'User {locators.username} has signed out.')


def sign_in(username, password):
    print('----- SIGN IN FUNCTION -----------------------------')
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.5)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)
    try:
        if driver.find_element(By.XPATH, f'//a/span[contains(., "{locators.username}")]'):
            sleep(0.25)
            print(f'User {locators.username} has signed in.')
        else:
            assert driver.find_element(By.XPATH, '//label[contains(., "Incorrect user name or password.")]')
            sleep(0.25)
            print('Error message displayed: Incorrect user name or password.')
    except NoSuchElementException as nse:
        print('Element not found.')
        print(f'User {locators.username} has not signed in.')


def delete_account():
    print('----- DELETE ACCOUNT FUNCTION -----------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'deletePopupBtn.deleteRed').click()
    sleep(2)
    print('User account has been deleted')




# setUp()
# register()
# check_fullname()
# check_orders()
# sign_out()
# sign_in(locators.username, locators.password)  # verify new credentials
# delete_account()
# sign_in(locators.username, locators.password)  # verify acct deleted - error label
# tearDown()
