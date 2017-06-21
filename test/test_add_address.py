# -*- coding: utf-8 -*-

from model.address import Address


def test_add_address(app):

    old_addresses = app.address.get_addresses_list()
    address = Address("ytredytrtrftyuf/./.", "Иванович", "Иванов", "ivan", "soft", "software", "г. Екатеринбург",
                         "8(343)2102101", "8(922)1234567", "8(343)7654321", "8(343)6543721", "ivanov@mail.ru",
                         "ivanov@ya.ru", "ivanov@rambler.ru", "ivanov.com", "г. Москва", "8(495)7654673", "йцукен")
    app.address.create(address)
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) + 1 == app.address.count()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)


def test_add_empty_address(app):

    old_addresses = app.address.get_addresses_list()
    address = Address()
    app.address.create(address)
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) + 1 == app.address.count()
    old_addresses.append(address)
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
