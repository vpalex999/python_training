# -*- coding: utf-8 -*-

from model.address import Address


def test_del_address(app):
    if not app.address.count():
        app.address.app.address.new_address_page()
        app.address.create(Address("Иван", "Иванович", "Иванов", "ivan", "soft", "software", "г. Екатеринбург",
                                   "8(343)2102101", "8(922)1234567", "8(343)7654321", "8(343)6543721", "ivanov@mail.ru",
                                   "ivanov@ya.ru", "ivanov@rambler.ru", "ivanov.com", "г. Москва", "8(495)7654673",
                                   "йцукен"))
        app.address.return_home_page()
    old_addresses = app.address.get_addresses_list()
    app.address.del_first_address()
    new_addresses = app.address.get_addresses_list()
    assert len(old_addresses) -1 == len(new_addresses)
    old_addresses[0:1] = []
    assert sorted(old_addresses, key=Address.id_or_max) == sorted(new_addresses, key=Address.id_or_max)
