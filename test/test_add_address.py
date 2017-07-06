# -*- coding: utf-8 -*-

from model.address import Address
# from data.addresses import testdata
# @pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])


def test_add_address(app, json_addresses):
    address = json_addresses
    old_addresses = app.address.get_addresses_list()
    app.address.create(address)
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) + 1 == app.address.count()
    address.name = address.name
    address.name = address.name
    address.lname = address.lname
    address.lname = address.lname
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)

