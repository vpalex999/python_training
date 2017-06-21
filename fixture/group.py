# -*- coding: utf-8 -*-

from model.group import Group

class GroupHelper(object):

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        # return to groups page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))):
            wd.find_element_by_link_text("group page").click()

    def return_home_page(self):
        """Return to home page"""
        wd = self.app.wd
        if not(wd.current_url.endswith("/addressbook/") and wd.find_element_by_name("searchstring")):
            wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()

    def create(self, group):
        # init group creation
        self.open_groups_page()
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        # fill group
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def fill_group_form(self, group):
        wd = self.app.wd

        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)
        # submit group edit

    def delete_first_group(self):
        # select first group
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletions
        wd.find_element_by_name("delete").click()
        self.return_home_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        """Modify first Group"""
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.return_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        """check count group"""
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements_by_css_selector("span.group"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups
