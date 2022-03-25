import unittest
import adshopcart_locators as locators
import adshopcart_methods as methods


class AdShopCartTestCases(unittest.TestCase):

    @staticmethod  # signal to Unittest that this is a function inside class (vs, @classmethod)
    def test_scenario():  # test in name is mandatory
        methods.setUp()

        methods.tearDown()
