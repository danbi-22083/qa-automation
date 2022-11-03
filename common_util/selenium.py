from selenium.webdriver.support import expected_conditions as seleniumEC
from selenium.webdriver.common.by import By


class seleniumFN(object):
    def findClickable(self, contentName):
        ec = seleniumEC.element_to_be_clickable(contentName)
        return ec

    def SlnBy(self, contentXpath):
        x = By.XPATH, contentXpath
        return x
