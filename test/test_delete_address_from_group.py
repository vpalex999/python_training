# -*- coding: utf-8 -*-

import random
from random import randrange

from model.group import Group
from model.address import Address
import pytest
from generator.address import testdata


@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_del_address_to_group(app, orm, address, check_ui):
    addresses_in_group = None
    if not len(orm.get_address_list()):
        app.address.create(address)

    if not len(orm.get_group_list()):
        app.group.create(Group(name="test"))

    if len(orm.get_all_address_to_group()) == 0:
        all_addresses = orm.get_address_list()
        all_group = orm.get_group_list()
        select_address = random.choice(all_addresses)
        select_group = random.choice(all_group)
        app.address.select_all_groups()
        app.address.selected_by_id(select_address.id)
        app.address.insert_address_in_group_by_id(select_group.id)

    all_group = orm.get_group_list()
    count_group = len(all_group)
    while count_group:
        select_group = random.choice(all_group)
        if len(select_group.name):
            addresses_in_group = orm.get_address_in_group(select_group)
            if len(addresses_in_group):
                break
            else:
                count_group -= 1
        else:
            count_group -= 1
    assert addresses_in_group is not None and len(addresses_in_group) != 0, "No contacts in groups"
    app.address.to_select_group(select_group.id)

    select_address = random.choice(addresses_in_group)
    app.address.selected_by_id(select_address.id)
    app.address.delete_address_from_group_by_id(select_address.id)
    new_addresses_in_group = orm.get_address_in_group(select_group)
    assert len(addresses_in_group) - 1 == len(new_addresses_in_group)
    if check_ui:
        orm_addr_in_gr = sorted(orm.get_address_in_group(select_group), key=Address.id_or_max)
        app_addr_in_gr = sorted(app.address.get_address_in_group(select_group), key=Address.id_or_max)
        assert orm_addr_in_gr == app_addr_in_gr


