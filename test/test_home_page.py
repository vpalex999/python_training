# -*- coding: utf-8 -*-

import re
from random import randrange
from model.address import Address


def test_view_contact_from_home_page(app):
    if not app.address.count():
        app.address.app.address.new_address_page()
        app.address.create(Address("Иван", "Иванович", "Иванов", "ivan", "soft", "software", "г. Екатеринбург",
                                   "8(343)2102101", "8(922)1234567", "8(343)7654321", "8(343)6543721", "ivanov@mail.ru",
                                   "ivanov@ya.ru", "ivanov@rambler.ru", "ivanov.com", "г. Москва", "8(495)7654673",
                                   "йцукен"))
        app.address.return_home_page()
    address_from_home_page = app.address.get_addresses_list()[0]
    address_from_edit_page = app.address.get_contact_info_from_edit_page(0)
    assert address_from_home_page.lname == address_from_edit_page.lname
    assert address_from_home_page.name == address_from_edit_page.name
    assert address_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(address_from_edit_page)
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)


def test_view_contact_from_home_page_by_index(app):
    if not app.address.count():
        app.address.app.address.new_address_page()
        app.address.create(Address("Иван", "Иванович", "Иванов", "ivan", "soft", "software", "г. Екатеринбург",
                                   "8(343)2102101", "8(922)1234567", "8(343)7654321", "8(343)6543721", "ivanov@mail.ru",
                                   "ivanov@ya.ru", "ivanov@rambler.ru", "ivanov.com", "г. Москва", "8(495)7654673",
                                   "йцукен"))
        app.address.return_home_page()
    old_addresses = app.address.get_addresses_list()
    index = randrange(len(old_addresses))
    address_from_home_page = old_addresses[index]
    address_from_edit_page = app.address.get_contact_info_from_edit_page(index)
    assert address_from_home_page.lname == address_from_edit_page.lname
    assert address_from_home_page.name == address_from_edit_page.name
    assert address_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(address_from_edit_page)
    assert address_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(address_from_edit_page)


def clear_phone(s):
    return re.sub("[() -]", "", s)


def merge_email_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [address.email, address.email2, address.email3])))


def merge_phones_like_on_home_page(address):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None, [address.phone, address.mobile,address.workphone , address.phone2]))))
