# -*- coding: utf-8 -*-

import re
from random import randrange
import random
import string
import pytest
from model.address import Address


def random_string(prefix, maxlen):
    symbols = f"{string.ascii_letters}{string.digits}"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Address(name="", mname="", lname="", nickname=random_string("nickname", 10))] + [
    Address(name=random_string("name", 10), mname=random_string("mname", 10), lname=random_string("lname", 10),
            nickname=random_string("nickname", 10),
            title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), phone=random_string("phone", 10),
            mobile=random_string("mobile", 10), workphone=random_string("workphone", 10),
            fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage=random_string("homepage", 10),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10),
            notes=random_string("notes", 10))
        for i in range(5)
    ]

@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_email_on_contact_view_page(app, address):
    if not app.address.count():
        app.address.create(address)
    old_addresses = app.address.get_addresses_list()
    index = randrange(len(old_addresses))
    address_from_home_page = old_addresses[index]
    address_from_edit_page = app.address.get_contact_info_from_edit_page(index)
    if address_from_home_page.all_email_from_home_page is None:
        address_from_home_page.all_email_from_home_page = ""
    address_from_home_page.all_email_from_home_page = clear(address_from_home_page.all_email_from_home_page)
    assert address_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(address_from_edit_page)


def clear(s):
    return re.sub("[() ]", "", s)

def merge_email_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [address.email, address.email2,address.email3]))))
