# -*- coding: utf-8 -*-

from random import randrange
import random
import string
import pytest
from model.address import Address


def random_string(prefix, maxlen):
    symbols = f"{string.ascii_letters}{string.digits}" + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
        Address(name=random_string("name", 10), lname=random_string("lname", 10))
    ]


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_del_random_address(app, address):
    if not app.address.count():
        app.address.create(address)
    old_addresses = app.address.get_addresses_list()
    index = randrange(len(old_addresses))
    app.address.del_address_by_index(index)
    assert len(old_addresses) -1 == app.address.count()


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_delete_all_addresses(app, address):
    if not app.address.count():
        app.address.create(address)
    app.address.del_all_address()
    assert len(app.address.get_addresses_list()) == 0


