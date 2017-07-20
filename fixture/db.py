# -*- coding: utf-8 -*-
import re
import mysql.connector
from model.group import Group
from model.address import Address

class DbFixture(object):
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group

    def get_address_list(self):
        addresses = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax, phone2) = row
                addresses.append(Address(id=str(id), name=firstname, lname=lastname, address=address, email=email,
                                       email2=email2, email3=email3,
                                       phone=home, mobile=mobile, workphone=work, fax=fax, phone2=phone2))
        finally:
            cursor.close()
        return addresses

    def destroy(self):
        self.connection.close()
