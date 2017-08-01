# -*- coding: utf-8 -*-

import pytest
import json
import os.path
from fixture.application import Application
from model.group import Group
from model.address import Address
from fixture.db import DbFixture



class AddressBook(object):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)


    def init_fixtures(self):
        web_config = self.target["web"]
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target["db"]
        self.dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                              password=db_config["password"])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def get_address_list(self):
        return self.dbfixture.get_address_list()

    def new_address(self, name, lname):
        return Address(name=name, lname=lname)

    def create_address(self, address):
        self.fixture.address.create(address)

    def address_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Address.id_or_max) == sorted(list2, key=Address.id_or_max)

    def delete_address(self, address):
        self.fixture.address.delete_address_by_id(address.id)

    def modify_address(self, new_address, address):
        self.fixture.address.update_address_by_id(new_address, address.id)
