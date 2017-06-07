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
        self.input_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        # submit deletions
        wd.find_element_by_name("delete").click()

    def edit_first_group(self, group):
        # edit first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        # edit fields
        self.input_fields(group)
        wd.find_element_by_name("update").click()

    def input_fields(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group edit




    def return_to_groups_page(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()