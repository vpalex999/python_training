# -*- coding: utf-8 -*-

from model.address import Address


def test_match_addresses(app, json_addresses, db, check_ui):
    address = json_addresses
    db_addresses_list = db.get_address_list()
    assert sorted(db_addresses_list, key=Address.id_or_max) == sorted(app.address.get_addresses_list(), key=Address.id_or_max)

