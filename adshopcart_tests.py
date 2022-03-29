import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AdShopCartTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs, @classmethod)
    def test_scenario():  # test in name is mandatory
        methods.setUp()
        methods.check_homepage()
        methods.register()
        methods.check_fullname()
        methods.check_orders()
        methods.sign_out()
        methods.sign_in(locators.username, locators.password)  # verify new credentials
        methods.delete_account()
        methods.sign_in(locators.username, locators.password)  # verify acct deleted - error label
        methods.tearDown()
