# -*- coding: utf-8 -*-

class GroupHelper(object):

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # init group creation
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()
        # fill group
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.app.wd

        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)
        # submit group edit

    def delete_first_group(self):
        # select first group
        wd = self.app.wd
        self.select_first_group()
        # submit deletions
        wd.find_element_by_name("delete").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        """Modify first Group"""
        wd = self.app.wd
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_groups_page(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def return_home_page(self):
        """Return to home page"""
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]/a").click()