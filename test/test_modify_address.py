# -*- coding: utf-8 -*-
from random import randrange
from model.address import Address
import random
import string
import pytest

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
def test_modify_address_by_range(app, address):
    if not app.address.count:
        app.address.create(address)
    old_addresses = app.address.get_addresses_list()
    index = randrange(len(old_addresses))
    address.id = old_addresses[index].id
    app.address.update_address_by_index(address, index)
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) == app.address.count()
    old_addresses[index] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)