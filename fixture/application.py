# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.address import AddressHelper


class Application(object):
    def __init__(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.address = AddressHelper(self)
        self.open_home_page()

    def open_home_page(self):
        # open homepage
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and wd.find_element_by_name("searchstring")):
            wd.get("http://localhost/addressbook/")


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

