# -*- coding: utf-8 -*-

from model.address import Address


def test_modify_address(app):
    old_addresses = app.address.get_addresses_list()
    address = Address("Иван1", "Иванович1", "Иванов1", "ivan1", "soft1", "software1", "г. Екатеринбург1",
                         "8(343)2102101-1", "8(922)1234567-1", "8(343)7654321-1", "8(343)6543721-1", "ivanov-1@mail.ru",
                         "ivanov-1@ya.ru", "ivanov-1@rambler.ru", "ivanov-1.com", "г. Москва-1", "8(495)7654673-1", "йцукен-1")

    address.id = old_addresses[0].id
    app.address.update_first_address(address)
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) == len(new_addresses)
    old_addresses[0] = address
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)

