# -*- coding: utf-8 -*-

import random
from random import randrange

from model.group import Group
from model.address import Address
import pytest
from generator.address import testdata


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_add_address_to_group(app, orm, address, check_ui):
    if not len(orm.get_address_list()):
        app.address.create(address)
    all_addresses = orm.get_address_list()
    all_group = orm.get_group_list()
    select_address = random.choice(all_addresses)
    select_group = random.choice(all_group)
    app.address.select_all_groups()
    app.address.selected_by_id(select_address.id)
    app.address.insert_address_in_group_by_id(select_group.id)
    assert select_address == orm.get_address_in_group_by_id(select_address, select_group)[0]
    if check_ui:
        orm_addr_in_gr = sorted(orm.get_address_in_group(select_group), key=Address.id_or_max)
        app_addr_in_gr = sorted(app.address.get_address_in_group(select_group), key=Address.id_or_max)
        assert orm_addr_in_gr == app_addr_in_gr
