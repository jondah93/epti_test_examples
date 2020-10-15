from core.page import Page


class EPTIHomePage(Page):

    def nav_bar(self):
        return self.driver.find_element_by_class_name("navigation")

    def nav_news(self):
        return self.nav_bar().find_element_by_link_text("News")

    def nav_ventures(self):
        return self.nav_bar().find_element_by_link_text("Ventures")

    def nav_career(self):
        return self.nav_bar().find_element_by_link_text("Career")

    def nav_about(self):
        return self.nav_bar().find_element_by_link_text("About us")
