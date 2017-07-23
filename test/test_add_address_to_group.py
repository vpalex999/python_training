# -*- coding: utf-8 -*-

import random
from random import randrange

from model.group import Group
import pytest
from generator.address import testdata


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, orm, address, check_ui):
    if not len(orm.get_address_list()):
        app.address.create(address)
    all_addresses = orm.get_address_list()
    all_group = orm.get_group_list()
    select_address = random.choice(all_addresses)
    select_group = random.choice(all_group)
    app.address.selected_by_id(select_address.id)
    app.address.insert_address_in_group_by_id(select_group.id)
    assert select_address == orm.get_address_in_group_by_id(select_address, select_group)[0]
