# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.address import Address


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return  fixture


def test_add_address(app):

    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.address.new_address_page()
    app.address.create(Address("Иван", "Иванович", "Иванов", "ivan", "soft", "software", "г. Екатеринбург",
                         "8(343)2102101", "8(922)1234567", "8(343)7654321", "8(343)6543721", "ivanov@mail.ru",
                         "ivanov@ya.ru", "ivanov@rambler.ru", "ivanov.com", "г. Москва", "8(495)7654673", "йцукен"))
    app.address.return_home_page()
    app.session.logout()
