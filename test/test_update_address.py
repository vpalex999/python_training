# -*- coding: utf-8 -*-

from model.address import Address


def test_update_address(app):

    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.address.update_first_contact(Address("Иван1", "Иванович1", "Иванов1", "ivan1", "soft1", "software1", "г. Екатеринбург1",
                         "8(343)2102101-1", "8(922)1234567-1", "8(343)7654321-1", "8(343)6543721-1", "ivanov-1@mail.ru",
                         "ivanov-1@ya.ru", "ivanov-1@rambler.ru", "ivanov-1.com", "г. Москва-1", "8(495)7654673-1", "йцукен-1"))

    app.session.logout()
