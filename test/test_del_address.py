# -*- coding: utf-8 -*-

from model.address import Address


def test_del_address(app):

    app.address.del_first_address()

