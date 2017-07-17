# -*- coding: utf-8 -*-

from model.address import Address


def test_add_address(app, json_addresses, db, check_ui):
    address = json_addresses
    old_addresses = db.get_address_list()
    app.address.create(address)
    old_addresses.append(address)
    assert len(old_addresses) == app.address.count()
    if check_ui:
        assert sorted(old_addresses, key=Address.id_or_max) == sorted(app.address.get_addresses_list(), key=Address.id_or_max)

