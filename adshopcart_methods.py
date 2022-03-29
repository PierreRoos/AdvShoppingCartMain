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
    print(f'----- setUp -------------------------------------------')
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


def check_homepage():
    print(f'----- check_homepage -----------------------------------')
    print('--- check SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, and MICE texts are displayed.')
    id_list = ['speakersTxt', 'tabletsTxt', 'headphonesTxt', 'laptopsTxt', 'miceTxt']
    title_list = ['SPEAKERS', 'TABLETS', 'HEADPHONES', 'LAPTOPS', 'MICE']

    for i in range(len(id_list)):
        id, title, = id_list[i], title_list[i]
        if driver.find_element(By.ID, id).is_displayed():
            sleep(0.5)
            print(f'{title} is displayed')

    print('--- check SPECIAL OFFER, POPULAR ITEMS, CONTACT US, and OUR PRODUCTS links at the top menu are clickable.')
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//h3[contains(., "SPECIAL OFFER")]')
    sleep(0.5)
    print('SPECIAL OFFER page is displayed')

    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//h3[contains(., "POPULAR ITEMS")]')
    sleep(0.5)
    print('POPULAR ITEMS page is displayed')

    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(0.5)
    assert driver.find_element(By.XPATH, '//h1[contains(., "CONTACT US")]')
    sleep(0.5)
    print('CONTACT US page is displayed')

    driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').click()
    sleep(0.5)
    assert driver.current_url == locators.hmpg_url  # homepage is products page
    sleep(0.5)
    print('OUR PRODUCTS page is homepage is displayed')

    print('--- Check main logo is displayed.')
    dvantage = driver.find_element(By.XPATH, '//span[contains(., "dvantage")]')
    demo = driver.find_element(By.XPATH, '//span[contains(., "DEMO")]')
    if dvantage and demo:
        sleep(0.5)
        print('Main logo is displayed')

    print('--- Check CONTACT US form works. Click CONTINUE SHOPPING button.')
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_index(2)
    sleep(0.5)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_index(2)
    sleep(0.5)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(0.5)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(0.5)
    # driver.find_element(By.LINK_TEXT, ' CONTINUE SHOPPING ').click()
    driver.find_element(By.XPATH, '//a[contains(., "CONTINUE SHOPPING")]').click()
    sleep(0.5)
    print('CONTACT US form was sent. We are back at the homepage.')


def register():
    print('----- register --------------------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(1)
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
    print('----- check_fullname -------------------------------------')
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
    print('----- check_orders -------------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, f'//label[contains(., "- No orders -" )]'):
        print(' This user has no orders. ')
    else:
        print('orders are not displayed. Check your code or website.')


def sign_out():
    print('----- sign_out --------------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(2)
    # driver.find_element(By.XPATH, '//label[contains(., "Sign out")]').click()  # doesnt work
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
    sleep(0.5)
    print(f'User {locators.username} has signed out.')


def sign_in(username, password):  # kind of works,not ideal
    print('----- sign_in --------------------------------------------')
    sleep(1)
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.5)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)
    # try:
    #     if driver.find_element(By.XPATH, f'//a/span[contains(., "{locators.username}")]'):
    #         sleep(0.25)
    #         print(f'User {locators.username} has signed in.')
    #     else: # won't ever go here
    #         assert driver.find_element(By.XPATH, '//label[contains(., "Incorrect user name or password.")]')
    #         sleep(0.25)
    #         print('Error message displayed: Incorrect user name or password.')
    # except NoSuchElementException as nse:
    #     print('Element not found.')
    #     print('Error message displayed: Incorrect user name or password.')
    #     print(f'User {locators.username} has not signed in.')

    if driver.find_element(By.XPATH, '//label[@id = "signInResultMessage"]').text == 'Incorrect user name or password.':
        # if driver.find_element(By.XPATH, '//label[contains(., "Incorrect user name or password.")]'): # gives error
        sleep(0.5)
        print('Error message displayed: Incorrect user name or password.')
    else:
        if driver.find_element(By.XPATH, f'//a/span[contains(., "{locators.username}")]'):
            sleep(0.5)
            print(f'User {locators.username} has signed in.')
        else:
            print(f'User {locators.username} has not signed in.')
            sleep(0.25)


def delete_account():
    print('----- delete_account -----------------------------------')
    driver.find_element(By.ID, 'menuUserLink').click()  # Click USER icon at top right of page
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, 'deletePopupBtn.deleteRed').click()
    sleep(2)
    print('User account has been deleted')


def tearDown():
    if driver is not None:
        print('----- tearDown() -------------------------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# setUp()
# check_homepage()
# register()
# check_fullname()
# check_orders()
# sign_out()
# sign_in(locators.username, locators.password)  # verify new credentials
# delete_account()
# sign_in(locators.username, locators.password)  # verify acct deleted - error label
# tearDown()
