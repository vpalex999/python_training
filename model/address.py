# -*- coding: utf-8 -*-

import re
from sys import maxsize


class Address:

    def __init__(self, name=None, mname=None, lname=None, nickname=None,\
                 title=None, company=None, address=None, phone=None, mobile=None, workphone=None,\
                 fax=None, email=None, email2=None, email3=None, homepage=None,\
                 address2=None, phone2=None, notes=None,\
                 id=None, all_phones_from_home_page=None, \
                 all_email_from_home_page=None, \
                 all_address_from_home_page=None):
        self.name = name
        self.mname = mname
        self.lname = lname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone = phone
        self.mobile = mobile
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_address_from_home_page = all_address_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return f"{self.name}, {self.lname}, {self.id}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and\
               (self.name is None or other.name is None or self.name == other.name) and\
               (self.lname is None or other.lname is None or self.lname == other.lname)