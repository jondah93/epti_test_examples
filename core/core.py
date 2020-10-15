import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Core(unittest.TestCase):

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")

    base_url = "url"

    def setUp(self):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
