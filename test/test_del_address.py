# -*- coding: utf-8 -*-

from model.address import Address


def test_add_address(app):

    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.address.del_first_contact()
    app.session.logout()
