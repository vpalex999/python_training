# -*- coding: utf-8 -*-

from random import randrange
import random
import string
import pytest
from model.address import Address
from generator.address import testdata


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_del_random_address(app, address, db, check_ui):
    if not len(db.get_address_list()):
        app.address.create(address)
    old_addresses = db.get_address_list()
    select_address = random.choice(old_addresses)
    app.address.delete_address_by_id(select_address.id)
    new_addresses = db.get_address_list()
    assert len(old_addresses) -1 == len(new_addresses)
    if check_ui:
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_addresses_list(),
                                                                      key=Address.id_or_max)


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_delete_all_addresses(app, address):
    if not app.address.count():
        app.address.create(address)
    app.address.del_all_address()
    assert len(app.address.get_addresses_list()) == 0


