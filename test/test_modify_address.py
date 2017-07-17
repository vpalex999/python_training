# -*- coding: utf-8 -*-

import random
from model.address import Address
import pytest
from generator.address import testdata


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_modify_address_by_range(app, address, db, check_ui):
    if not len(db.get_address_list()):
        app.address.create(address)
    old_addresses = db.get_address_list()
    select_address = random.choice(old_addresses)
    app.address.update_address_by_id(address, select_address.id)
    new_addresses = db.get_address_list()
    assert len(old_addresses) == len(new_addresses)
    if check_ui:
        assert sorted(new_addresses, key=Address.id_or_max) == sorted(app.address.get_addresses_list(), key=Address.id_or_max)
