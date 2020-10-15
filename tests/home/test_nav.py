from core.core import Core
from pages import epti_home


class NavTests(Core):
    """
    Test that the navbar buttons redirect to the
    correct url as well as elements being set to active.
    """

    base_url = "https://epti.com"

    def setUp(self):
        super().setUp()
        self.driver.get(self.base_url)
        self.home = epti_home.EPTIHomePage(self.driver)

    def test_nav_news(self):
        self.home.nav_news().click()
        self.assertTrue("active" in self.home.nav_news().find_element_by_xpath("..").get_attribute("class"))
        self.assertTrue("news" in self.driver.current_url)

    def test_nav_ventures(self):
        self.home.nav_ventures().click()
        self.assertTrue("active" in self.home.nav_ventures().find_element_by_xpath("..").get_attribute("class"))
        self.assertTrue("ventures" in self.driver.current_url)

    def test_nav_career(self):
        self.home.nav_career().click()
        self.assertTrue("active" in self.home.nav_career().find_element_by_xpath("..").get_attribute("class"))
        self.assertTrue("career" in self.driver.current_url)

    def test_nav_about(self):
        self.home.nav_about().click()
        self.assertTrue("active" in self.home.nav_about().find_element_by_xpath("..").get_attribute("class"))
        self.assertTrue("about" in self.driver.current_url)
