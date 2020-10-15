from selenium.webdriver.remote.errorhandler import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Page(object):

    ignored_exceptions = [
        ElementNotVisibleException,
        ElementNotSelectableException,
        ElementNotInteractableException,
        ElementClickInterceptedException,
        UnexpectedAlertPresentException,
        WebDriverException,
        TimeoutException,
    ]

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1, ignored_exceptions=self.ignored_exceptions)
        self.actions = ActionChains(self.driver)
