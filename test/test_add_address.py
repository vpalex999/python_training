# -*- coding: utf-8 -*-

import pytest

from address import Address
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return  fixture


def test_add_address(app):

    app.open_home_page()
    app.login(username="admin", password="secret")
    app.open_new_address_page()
    app.add_new_address(Address("Иван", "Иванович", "Иванов", "ivan", "soft", "software", "г. Екатеринбург",
                         "8(343)2102101", "8(922)1234567", "8(343)7654321", "8(343)6543721", "ivanov@mail.ru",
                         "ivanov@ya.ru", "ivanov@rambler.ru", "ivanov.com", "г. Москва", "8(495)7654673", "йцукен"))
    app.return_home_page()
    app.logout()
